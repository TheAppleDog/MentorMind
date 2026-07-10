from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from ..models.models import (
    db, User, Session, Task, Feedback, SkillTracking, 
    MentorMapping, CareerRoadmap, Notification, Announcement
)
from datetime import datetime, timedelta

student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    # Get assigned mentor
    mentor_mapping = MentorMapping.query.filter_by(
        student_id=current_user.user_id, 
        status='active'
    ).first()
    
    mentor = None
    if mentor_mapping:
        mentor = User.query.get(mentor_mapping.mentor_id)
    
    # Get upcoming sessions
    upcoming_sessions = Session.query.filter(
        Session.student_id == current_user.user_id,
        Session.session_date >= datetime.now().date(),
        Session.status == 'scheduled'
    ).order_by(Session.session_date).limit(5).all()
    
    # Get active tasks
    active_tasks = Task.query.filter(
        Task.student_id == current_user.user_id,
        Task.status != 'completed'
    ).all()
    
    # Get recent announcements
    announcements = Announcement.query.filter(
        Announcement.target_audience.in_(['students', 'all'])
    ).order_by(Announcement.announcement_date.desc()).limit(5).all()
    
    return render_template('student/dashboard.html', 
                          mentor=mentor, 
                          upcoming_sessions=upcoming_sessions,
                          active_tasks=active_tasks,
                          announcements=announcements)

@student_bp.route('/sessions', methods=['GET', 'POST'])
@login_required
def sessions():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        mentor_id = request.form.get('mentor_id')
        session_date = request.form.get('session_date')
        session_time = request.form.get('session_time')
        topic = request.form.get('topic')
        description = request.form.get('description')
        
        try:
            session = Session(
                student_id=current_user.user_id,
                mentor_id=mentor_id,
                session_date=datetime.strptime(session_date, '%Y-%m-%d').date(),
                session_time=datetime.strptime(session_time, '%H:%M').time(),
                topic=topic,
                description=description,
                status='scheduled'
            )
            db.session.add(session)
            db.session.commit()
            flash('Session scheduled successfully!', 'success')
            return redirect(url_for('student.sessions'))
        except Exception as e:
            flash(f'Error scheduling session: {str(e)}', 'danger')
            db.session.rollback()
    
    # Get all sessions
    all_sessions = Session.query.filter_by(student_id=current_user.user_id).all()
    
    # Get assigned mentor
    mentor_mapping = MentorMapping.query.filter_by(
        student_id=current_user.user_id,
        status='active'
    ).first()
    
    return render_template('student/sessions.html', 
                          sessions=all_sessions,
                          mentor_id=mentor_mapping.mentor_id if mentor_mapping else None)

@student_bp.route('/progress')
@login_required
def progress():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    # Get skills
    skills = SkillTracking.query.filter_by(student_id=current_user.user_id).all()
    
    # Get tasks
    tasks = Task.query.filter_by(student_id=current_user.user_id).all()
    
    # Calculate statistics
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.status == 'completed'])
    
    return render_template('student/progress.html', 
                          skills=skills,
                          tasks=tasks,
                          total_tasks=total_tasks,
                          completed_tasks=completed_tasks)

@student_bp.route('/feedback/<int:session_id>', methods=['GET', 'POST'])
@login_required
def provide_feedback(session_id):
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    session = Session.query.get_or_404(session_id)
    
    if session.student_id != current_user.user_id:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        
        try:
            feedback = Feedback(
                session_id=session_id,
                student_id=current_user.user_id,
                mentor_id=session.mentor_id,
                rating=int(rating),
                comment=comment
            )
            db.session.add(feedback)
            db.session.commit()
            flash('Feedback submitted successfully!', 'success')
            return redirect(url_for('student.sessions'))
        except Exception as e:
            flash(f'Error submitting feedback: {str(e)}', 'danger')
            db.session.rollback()
    
    return render_template('student/feedback.html', session=session)

@student_bp.route('/career-roadmap')
@login_required
def career_roadmap():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    roadmap = CareerRoadmap.query.filter_by(student_id=current_user.user_id).first()
    
    return render_template('student/career_roadmap.html', roadmap=roadmap)

@student_bp.route('/profile')
@login_required
def profile():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))
    
    return render_template('student/profile.html', user=current_user)

@student_bp.route('/notifications')
@login_required
def notifications():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))

    from datetime import date
    notifications = Notification.query.filter(
        Notification.user_id == current_user.user_id,
        Notification.created_at >= date.today()
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template('student/notifications.html', notifications=notifications)

@student_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if current_user.role != 'student':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'update_profile':
            current_user.first_name = request.form.get('first_name')
            current_user.last_name = request.form.get('last_name')
            current_user.phone = request.form.get('phone')
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('student.settings'))

        elif action == 'change_password':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')

            if not current_user.check_password(current_password):
                flash('Current password is incorrect', 'danger')
                return redirect(url_for('student.settings'))

            if new_password != confirm_password:
                flash('New passwords do not match', 'danger')
                return redirect(url_for('student.settings'))

            current_user.set_password(new_password)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('student.settings'))

    return render_template('student/settings.html', user=current_user)

@student_bp.route('/api/notifications/unread_count')
@login_required
def unread_count():
    if current_user.role not in ['student', 'mentor', 'admin']:
        return jsonify({'error': 'Unauthorized'}), 401
    from datetime import datetime, timedelta
    count = Notification.query.filter(
        Notification.user_id == current_user.user_id, 
        Notification.is_read == False,
        Notification.created_at >= datetime.utcnow() - timedelta(days=1)
    ).count()
    return jsonify({'count': count})

@student_bp.route('/api/notifications/unread')
@login_required
def unread_notifications():
    if current_user.role not in ['student', 'mentor', 'admin']:
        return jsonify({'error': 'Unauthorized'}), 401
    from datetime import datetime, timedelta
    notifs = Notification.query.filter(
        Notification.user_id == current_user.user_id, 
        Notification.is_read == False,
        Notification.created_at >= datetime.utcnow() - timedelta(days=1)
    ).order_by(Notification.created_at.desc()).limit(10).all()
    return jsonify([{
        'id': n.notification_id,
        'title': n.title,
        'message': n.message,
        'type': n.notification_type,
        'created_at': n.created_at.isoformat()
    } for n in notifs])

@student_bp.route('/api/notifications/read/<int:notif_id>', methods=['POST'])
@login_required
def mark_read(notif_id):
    if current_user.role not in ['student', 'mentor', 'admin']:
        return jsonify({'error': 'Unauthorized'}), 401
    notif = Notification.query.filter_by(
        notification_id=notif_id, 
        user_id=current_user.user_id
    ).first_or_404()
    notif.is_read = True
    db.session.commit()
    return jsonify({'success': True})

@student_bp.route('/api/notifications/read_all', methods=['POST'])
@login_required
def mark_all_read():
    if current_user.role not in ['student', 'mentor', 'admin']:
        return jsonify({'error': 'Unauthorized'}), 401
    count = db.session.query(Notification).filter_by(
        user_id=current_user.user_id, 
        is_read=False
    ).update({Notification.is_read: True})
    db.session.commit()
    return jsonify({'success': True, 'cleared': count})
