from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from ..models.models import (
    db, User, Session, Task, Feedback, MentorMapping, 
    SkillTracking, Notification, SessionNotes, MentorQuality, MentorProfile, RiskAlert
)
from datetime import datetime, timedelta

mentor_bp = Blueprint('mentor', __name__)

@mentor_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    # Get assigned students
    mentor_mappings = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        status='active'
    ).all()
    
    students = [User.query.get(mapping.student_id) for mapping in mentor_mappings]
    
    # Get upcoming sessions
    upcoming_sessions = Session.query.filter(
        Session.mentor_id == current_user.user_id,
        Session.session_date >= datetime.now().date(),
        Session.status == 'scheduled'
    ).order_by(Session.session_date).limit(5).all()
    
    # Get pending tasks
    pending_tasks = Task.query.filter(
        Task.mentor_id == current_user.user_id,
        Task.status != 'completed'
    ).all()
    
    # Get at-risk students for dashboard
    at_risk_students = []
    for mapping in mentor_mappings:
        student = User.query.get(mapping.student_id)
        risk_data = calculate_student_risk(student.user_id, current_user.user_id)
        if risk_data['risk_level'] in ['medium', 'high', 'critical']:
            at_risk_students.append({
                'student': student,
                'risk_level': risk_data['risk_level'],
                'session_attendance_rate': risk_data['session_attendance_rate'],
                'task_completion_rate': risk_data['task_completion_rate'],
                'avg_feedback_score': risk_data['avg_feedback_score'],
                'progress_rate': risk_data['progress_rate'],
                'risk_factors': risk_data['risk_factors']
            })
    
    # Sort by risk level
    level_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    at_risk_students.sort(key=lambda x: level_order.get(x['risk_level'], 3))
    
    return render_template('mentor/dashboard.html',
                          students=students,
                          upcoming_sessions=upcoming_sessions,
                          pending_tasks=pending_tasks,
                          at_risk_students=at_risk_students)

@mentor_bp.route('/students')
@login_required
def students():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    mentor_mappings = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        status='active'
    ).all()
    
    students = [User.query.get(mapping.student_id) for mapping in mentor_mappings]
    
    return render_template('mentor/students.html', students=students)

@mentor_bp.route('/student/<int:student_id>')
@login_required
def student_detail(student_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    # Verify mentor-student relationship
    mapping = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        student_id=student_id
    ).first_or_404()
    
    student = User.query.get_or_404(student_id)
    
    # Get student's tasks
    tasks = Task.query.filter_by(student_id=student_id).all()
    
    # Get student's skills
    skills = SkillTracking.query.filter_by(student_id=student_id).all()
    
    # Get session history
    sessions = Session.query.filter_by(
        student_id=student_id,
        mentor_id=current_user.user_id
    ).all()
    
    return render_template('mentor/student_detail.html',
                          student=student,
                          tasks=tasks,
                          skills=skills,
                          sessions=sessions)

@mentor_bp.route('/assign-task/<int:student_id>', methods=['GET', 'POST'])
@login_required
def assign_task(student_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    # Verify relationship
    mapping = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        student_id=student_id
    ).first_or_404()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        deadline = request.form.get('deadline')
        priority = request.form.get('priority')
        
        try:
            task = Task(
                student_id=student_id,
                mentor_id=current_user.user_id,
                title=title,
                description=description,
                deadline=datetime.strptime(deadline, '%Y-%m-%d').date() if deadline else None,
                priority=priority,
                status='pending'
            )
            db.session.add(task)
            db.session.commit()
            
            # Create notification
            notification = Notification(
                user_id=student_id,
                title='New Task Assigned',
                message=f'Your mentor assigned a new task: {title}',
                notification_type='task'
            )
            db.session.add(notification)
            db.session.commit()
            
            flash('Task assigned successfully!', 'success')
            return redirect(url_for('mentor.student_detail', student_id=student_id))
        except Exception as e:
            flash(f'Error assigning task: {str(e)}', 'danger')
            db.session.rollback()
    
    student = User.query.get_or_404(student_id)
    return render_template('mentor/assign_task.html', student=student)

@mentor_bp.route('/sessions')
@login_required
def sessions():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    sessions = Session.query.filter_by(mentor_id=current_user.user_id).all()
    
    return render_template('mentor/sessions.html', sessions=sessions)

@mentor_bp.route('/feedback/<int:student_id>')
@login_required
def student_feedback(student_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    # Verify relationship
    mapping = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        student_id=student_id
    ).first_or_404()
    
    feedback_list = Feedback.query.filter_by(
        student_id=student_id,
        mentor_id=current_user.user_id
    ).all()
    
    return render_template('mentor/student_feedback.html',
                          student_id=student_id,
                          feedback=feedback_list)

@mentor_bp.route('/sessions/approve/<int:session_id>', methods=['POST'])
@login_required
def approve_session(session_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    session = Session.query.get_or_404(session_id)
    
    if session.mentor_id != current_user.user_id:
        return redirect(url_for('auth.login'))
    
    try:
        session.approval_status = 'approved'
        session.status = 'approved'
        db.session.commit()
        
        # Notify student
        notification = Notification(
            user_id=session.student_id,
            title='Session Approved',
            message=f'Your mentoring session on {session.session_date} has been approved',
            notification_type='approval'
        )
        db.session.add(notification)
        db.session.commit()
        
        flash('Session approved successfully', 'success')
    except Exception as e:
        flash(f'Error approving session: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('mentor.sessions'))

@mentor_bp.route('/sessions/reject/<int:session_id>', methods=['POST'])
@login_required
def reject_session(session_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    session = Session.query.get_or_404(session_id)
    
    if session.mentor_id != current_user.user_id:
        return redirect(url_for('auth.login'))
    
    reason = request.form.get('reason', '')
    
    try:
        session.approval_status = 'rejected'
        session.status = 'rejected'
        db.session.commit()
        
        # Notify student
        notification = Notification(
            user_id=session.student_id,
            title='Session Rejected',
            message=f'Your session request has been rejected. Reason: {reason}',
            notification_type='rejection'
        )
        db.session.add(notification)
        db.session.commit()
        
        flash('Session rejected', 'info')
    except Exception as e:
        flash(f'Error rejecting session: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('mentor.sessions'))

@mentor_bp.route('/sessions/reschedule/<int:session_id>', methods=['GET', 'POST'])
@login_required
def reschedule_session(session_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    session = Session.query.get_or_404(session_id)
    
    if session.mentor_id != current_user.user_id:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        new_date = request.form.get('session_date')
        new_time = request.form.get('session_time')
        reason = request.form.get('reason')
        
        try:
            session.session_date = datetime.strptime(new_date, '%Y-%m-%d').date()
            session.session_time = datetime.strptime(new_time, '%H:%M').time()
            session.status = 'rescheduled'
            db.session.commit()
            
            # Notify student
            notification = Notification(
                user_id=session.student_id,
                title='Session Rescheduled',
                message=f'Your session has been rescheduled to {new_date} at {new_time}',
                notification_type='reschedule'
            )
            db.session.add(notification)
            db.session.commit()
            
            flash('Session rescheduled successfully', 'success')
            return redirect(url_for('mentor.sessions'))
        except Exception as e:
            flash(f'Error rescheduling: {str(e)}', 'danger')
            db.session.rollback()
    
    return render_template('mentor/reschedule_session.html', session=session)

@mentor_bp.route('/sessions/<int:session_id>/add-notes', methods=['GET', 'POST'])
@login_required
def add_session_notes(session_id):
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    session = Session.query.get_or_404(session_id)
    
    if session.mentor_id != current_user.user_id:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        notes = request.form.get('notes')
        student_progress = request.form.get('student_progress')
        next_focus = request.form.get('next_focus_areas')
        
        try:
            session_note = SessionNotes(
                session_id=session_id,
                mentor_id=current_user.user_id,
                notes=notes,
                student_progress=student_progress,
                next_focus_areas=next_focus
            )
            db.session.add(session_note)
            session.mentor_notes = notes
            session.status = 'completed'
            db.session.commit()
            
            flash('Notes added successfully', 'success')
            return redirect(url_for('mentor.sessions'))
        except Exception as e:
            flash(f'Error adding notes: {str(e)}', 'danger')
            db.session.rollback()
    
    return render_template('mentor/add_session_notes.html', session=session)

@mentor_bp.route('/analytics')
@login_required
def analytics():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))
    
    # Get mentor quality metrics
    mentor_quality = MentorQuality.query.filter_by(mentor_id=current_user.user_id).first()
    
    # Get all mentee sessions
    mentor_mappings = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        status='active'
    ).all()
    
    mentees = [User.query.get(mapping.student_id) for mapping in mentor_mappings]
    
    # Get performance data
    total_sessions = Session.query.filter_by(mentor_id=current_user.user_id).count()
    completed_sessions = Session.query.filter_by(
        mentor_id=current_user.user_id,
        status='completed'
    ).count()
    
    avg_feedback = db.session.query(db.func.avg(Feedback.rating)).filter(
        Feedback.mentor_id == current_user.user_id
    ).scalar() or 0
    
    # Get mentee performance
    mentee_stats = []
    for mentee in mentees:
        tasks = Task.query.filter_by(student_id=mentee.user_id).all()
        completed_tasks = len([t for t in tasks if t.status == 'completed'])
        total_tasks = len(tasks)
        completion_rate = ((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
        
        mentee_stats.append({
            'student': mentee,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'completion_rate': completion_rate
        })
    
    return render_template('mentor/analytics.html',
                          mentor_quality=mentor_quality,
                          mentee_stats=mentee_stats,
                          total_sessions=total_sessions,
                          completed_sessions=completed_sessions,
                          avg_feedback=avg_feedback)

@mentor_bp.route('/profile')
@login_required
def profile():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))

    return render_template('mentor/profile.html', user=current_user)

@mentor_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'update_profile':
            current_user.first_name = request.form.get('first_name')
            current_user.last_name = request.form.get('last_name')
            current_user.phone = request.form.get('phone')
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('mentor.settings'))

        elif action == 'change_password':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')

            if not current_user.check_password(current_password):
                flash('Current password is incorrect', 'danger')
                return redirect(url_for('mentor.settings'))

            if new_password != confirm_password:
                flash('New passwords do not match', 'danger')
                return redirect(url_for('mentor.settings'))

            current_user.set_password(new_password)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('mentor.settings'))

@mentor_bp.route('/notifications')
@login_required
def notifications():
    if current_user.role != 'mentor':
        return redirect(url_for('auth.login'))

    from datetime import date
    notifications = Notification.query.filter(
        Notification.user_id == current_user.user_id,
        Notification.created_at >= date.today()
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template('mentor/notifications.html', notifications=notifications)


# ==================== Risk Detection Functions ====================

def calculate_student_risk(student_id, mentor_id):
    """
    Calculate risk metrics for a student.
    Returns a dictionary with risk metrics and level.
    """
    # Get all sessions for this student with this mentor
    sessions = Session.query.filter_by(
        student_id=student_id,
        mentor_id=mentor_id
    ).all()
    
    # Calculate session attendance rate
    total_sessions = len(sessions)
    if total_sessions > 0:
        completed_sessions = len([s for s in sessions if s.status == 'completed'])
        cancelled_sessions = len([s for s in sessions if s.status == 'cancelled'])
        # Attendance rate = (completed / total) * 100
        session_attendance_rate = (completed_sessions / total_sessions) * 100
    else:
        session_attendance_rate = 100.0  # No sessions yet, assume 100%
    
    # Calculate task completion rate
    tasks = Task.query.filter_by(student_id=student_id).all()
    total_tasks = len(tasks)
    if total_tasks > 0:
        completed_tasks = len([t for t in tasks if t.status == 'completed'])
        task_completion_rate = (completed_tasks / total_tasks) * 100
    else:
        task_completion_rate = 100.0  # No tasks yet, assume 100%
    
    # Calculate average feedback score
    feedback_list = Feedback.query.filter_by(
        student_id=student_id,
        mentor_id=mentor_id
    ).all()
    
    if feedback_list:
        avg_feedback_score = sum([f.rating for f in feedback_list]) / len(feedback_list)
    else:
        avg_feedback_score = 5.0  # No feedback yet, assume 5 (best)
    
    # Calculate progress rate based on skills
    skills = SkillTracking.query.filter_by(student_id=student_id).all()
    if skills:
        progress_rate = sum([s.proficiency_score for s in skills]) / len(skills)
    else:
        progress_rate = 100.0  # No skills tracked yet, assume 100%
    
    # Determine risk factors
    risk_factors = []
    
    if session_attendance_rate < 70:
        risk_factors.append('low_attendance')
    elif session_attendance_rate < 85:
        risk_factors.append('declining_attendance')
    
    if task_completion_rate < 60:
        risk_factors.append('missed_deadlines')
    elif task_completion_rate < 80:
        risk_factors.append('delayed_tasks')
    
    if avg_feedback_score < 3:
        risk_factors.append('poor_feedback')
    elif avg_feedback_score < 4:
        risk_factors.append('average_feedback')
    
    if progress_rate < 50:
        risk_factors.append('stalled_progress')
    elif progress_rate < 75:
        risk_factors.append('slow_progress')
    
    # Calculate overall risk level
    risk_score = 0
    risk_score += (100 - session_attendance_rate) * 0.3  # 30% weight
    risk_score += (100 - task_completion_rate) * 0.3     # 30% weight
    risk_score += (5 - avg_feedback_score) * 10 * 0.2   # 20% weight
    risk_score += (100 - progress_rate) * 0.2          # 20% weight
    
    # Determine risk level based on score
    if risk_score >= 60:
        risk_level = 'critical'
    elif risk_score >= 40:
        risk_level = 'high'
    elif risk_score >= 20:
        risk_level = 'medium'
    else:
        risk_level = 'low'
    
    # Generate recommendations
    recommendations = []
    if session_attendance_rate < 85:
        recommendations.append("Schedule a meeting to discuss attendance challenges")
    if task_completion_rate < 80:
        recommendations.append("Break down tasks into smaller, manageable steps")
    if avg_feedback_score < 4:
        recommendations.append("Discuss areas for improvement in upcoming sessions")
    if progress_rate < 75:
        recommendations.append("Create a structured learning plan with milestones")
    
    if not recommendations:
        recommendations.append("Continue monitoring progress - student is performing well")
    
    return {
        'session_attendance_rate': round(session_attendance_rate, 2),
        'task_completion_rate': round(task_completion_rate, 2),
        'avg_feedback_score': round(avg_feedback_score, 2),
        'progress_rate': round(progress_rate, 2),
        'risk_factors': risk_factors,
        'risk_level': risk_level,
        'risk_score': round(risk_score, 2),
        'recommendations': recommendations
    }


def create_or_update_risk_alert(student_id, mentor_id, risk_data):
    """
    Create or update a risk alert for a student.
    """
    # Check if an active alert already exists
    existing_alert = RiskAlert.query.filter_by(
        student_id=student_id,
        mentor_id=mentor_id,
        status='active'
    ).first()
    
    if existing_alert:
        # Update existing alert
        previous_level = existing_alert.risk_level
        existing_alert.risk_level = risk_data['risk_level']
        existing_alert.session_attendance_rate = risk_data['session_attendance_rate']
        existing_alert.task_completion_rate = risk_data['task_completion_rate']
        existing_alert.avg_feedback_score = risk_data['avg_feedback_score']
        existing_alert.progress_rate = risk_data['progress_rate']
        existing_alert.risk_factors = risk_data['risk_factors']
        existing_alert.recommendations = '; '.join(risk_data['recommendations'])
        existing_alert.updated_at = datetime.utcnow()
        
        # Notify mentor if risk level increased
        if risk_level_increased(previous_level, risk_data['risk_level']):
            notify_mentor_risk_alert(existing_alert, previous_level)
        
        return existing_alert
    else:
        # Create new alert
        new_alert = RiskAlert(
            student_id=student_id,
            mentor_id=mentor_id,
            risk_level=risk_data['risk_level'],
            status='active',
            session_attendance_rate=risk_data['session_attendance_rate'],
            task_completion_rate=risk_data['task_completion_rate'],
            avg_feedback_score=risk_data['avg_feedback_score'],
            progress_rate=risk_data['progress_rate'],
            risk_factors=risk_data['risk_factors'],
            recommendations='; '.join(risk_data['recommendations'])
        )
        
        # Notify mentor if student is at risk
        if risk_data['risk_level'] in ['high', 'critical']:
            notify_mentor_risk_alert(new_alert, None)
        
        return new_alert


def risk_level_increased(previous_level, new_level):
    """Check if risk level has increased."""
    levels = {'low': 0, 'medium': 1, 'high': 2, 'critical': 3}
    return levels.get(new_level, 0) > levels.get(previous_level, 0)


def notify_mentor_risk_alert(alert, previous_level):
    """Send notification to mentor about risk alert."""
    student = User.query.get(alert.student_id)
    
    if previous_level:
        message = f"Risk level for {student.name} has increased from {previous_level} to {alert.risk_level}"
    else:
        message = f"Student {student.name} has been flagged as '{alert.risk_level}' risk"
    
    notification = Notification(
        user_id=alert.mentor_id,
        title='At-Risk Student Alert',
        message=message,
        notification_type='risk_alert'
    )
    db.session.add(notification)
    db.session.commit()


# ==================== Risk Detection API Routes ====================

@mentor_bp.route('/api/students/<int:student_id>/risk')
@login_required
def get_student_risk(student_id):
    """Get risk assessment for a specific student."""
    if current_user.role != 'mentor':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Verify mentor-student relationship
    mapping = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        student_id=student_id
    ).first()
    
    if not mapping:
        return jsonify({'error': 'Student not assigned to you'}), 404
    
    # Check if there's an existing risk alert
    risk_alert = RiskAlert.query.filter_by(
        student_id=student_id,
        mentor_id=current_user.user_id,
        status='active'
    ).first()
    
    if risk_alert:
        return jsonify({
            'student_id': student_id,
            'risk_level': risk_alert.risk_level,
            'session_attendance_rate': risk_alert.session_attendance_rate,
            'task_completion_rate': risk_alert.task_completion_rate,
            'avg_feedback_score': risk_alert.avg_feedback_score,
            'progress_rate': risk_alert.progress_rate,
            'risk_factors': risk_alert.risk_factors or [],
            'recommendations': risk_alert.recommendations,
            'created_at': risk_alert.created_at.isoformat() if risk_alert.created_at else None,
            'updated_at': risk_alert.updated_at.isoformat() if risk_alert.updated_at else None
        })
    
    # Calculate fresh risk data
    risk_data = calculate_student_risk(student_id, current_user.user_id)
    
    return jsonify({
        'student_id': student_id,
        'risk_level': risk_data['risk_level'],
        'session_attendance_rate': risk_data['session_attendance_rate'],
        'task_completion_rate': risk_data['task_completion_rate'],
        'avg_feedback_score': risk_data['avg_feedback_score'],
        'progress_rate': risk_data['progress_rate'],
        'risk_factors': risk_data['risk_factors'],
        'recommendations': risk_data['recommendations']
    })


@mentor_bp.route('/api/students/risk/all')
@login_required
def get_all_student_risks():
    """Get risk assessments for all students assigned to the mentor."""
    if current_user.role != 'mentor':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Get all assigned students
    mentor_mappings = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        status='active'
    ).all()
    
    at_risk_students = []
    
    for mapping in mentor_mappings:
        student = User.query.get(mapping.student_id)
        
        # Get or calculate risk data
        risk_alert = RiskAlert.query.filter_by(
            student_id=student.user_id,
            mentor_id=current_user.user_id,
            status='active'
        ).first()
        
        if risk_alert:
            risk_data = {
                'student_id': student.user_id,
                'student_name': student.name,
                'student_email': student.email,
                'risk_level': risk_alert.risk_level,
                'session_attendance_rate': risk_alert.session_attendance_rate,
                'task_completion_rate': risk_alert.task_completion_rate,
                'avg_feedback_score': risk_alert.avg_feedback_score,
                'progress_rate': risk_alert.progress_rate,
                'risk_factors': risk_alert.risk_factors or [],
                'alert_id': risk_alert.alert_id
            }
        else:
            # Calculate fresh risk data
            risk_calc = calculate_student_risk(student.user_id, current_user.user_id)
            risk_data = {
                'student_id': student.user_id,
                'student_name': student.name,
                'student_email': student.email,
                'risk_level': risk_calc['risk_level'],
                'session_attendance_rate': risk_calc['session_attendance_rate'],
                'task_completion_rate': risk_calc['task_completion_rate'],
                'avg_feedback_score': risk_calc['avg_feedback_score'],
                'progress_rate': risk_calc['progress_rate'],
                'risk_factors': risk_calc['risk_factors'],
                'alert_id': None
            }
        
        # Include at-risk students (medium, high, critical)
        if risk_data['risk_level'] in ['medium', 'high', 'critical']:
            at_risk_students.append(risk_data)
    
    # Sort by risk level (critical first)
    level_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    at_risk_students.sort(key=lambda x: level_order.get(x['risk_level'], 3))
    
    return jsonify({
        'total_students': len(mentor_mappings),
        'at_risk_count': len(at_risk_students),
        'at_risk_students': at_risk_students
    })


@mentor_bp.route('/api/students/risk/refresh', methods=['POST'])
@login_required
def refresh_all_risks():
    """Recalculate risk for all students assigned to the mentor."""
    if current_user.role != 'mentor':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Get all assigned students
    mentor_mappings = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        status='active'
    ).all()
    
    updated_count = 0
    new_alerts = 0
    
    for mapping in mentor_mappings:
        student_id = mapping.student_id
        
        # Calculate fresh risk data
        risk_data = calculate_student_risk(student_id, current_user.user_id)
        
        # Create or update risk alert
        alert = create_or_update_risk_alert(student_id, current_user.user_id, risk_data)
        
        if alert:
            if alert.created_at == alert.updated_at or (alert.updated_at - alert.created_at).seconds < 5:
                new_alerts += 1
            else:
                updated_count += 1
            db.session.add(alert)
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'Risk assessment completed. {new_alerts} new alerts, {updated_count} updated.',
        'total_students': len(mentor_mappings)
    })


@mentor_bp.route('/api/students/<int:student_id>/risk/resolve', methods=['POST'])
@login_required
def resolve_student_risk(student_id):
    """Mark a risk alert as resolved."""
    if current_user.role != 'mentor':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Verify mentor-student relationship
    mapping = MentorMapping.query.filter_by(
        mentor_id=current_user.user_id,
        student_id=student_id
    ).first()
    
    if not mapping:
        return jsonify({'error': 'Student not assigned to you'}), 404
    
    # Find and resolve the alert
    risk_alert = RiskAlert.query.filter_by(
        student_id=student_id,
        mentor_id=current_user.user_id,
        status='active'
    ).first()
    
    if risk_alert:
        risk_alert.status = 'resolved'
        risk_alert.resolved_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Risk alert marked as resolved'
        })
    
    return jsonify({'error': 'No active risk alert found'}), 404
