from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from ..models.models import (
    db, User, Session, MentorMapping, Announcement, 
    Feedback, Task, Notification, MentorProfile, MentorQuality,
    StudentProfile, PlatformSettings
)
from datetime import datetime, timedelta
from sqlalchemy import func

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page - separate from user login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            if user.role != 'admin':
                flash('Access denied. Admin credentials required.', 'error')
                return redirect(url_for('admin.login'))
            
            login_user(user, remember=request.form.get('remember'))
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    # Get statistics
    total_students = User.query.filter_by(role='student').count()
    total_mentors = User.query.filter_by(role='mentor').count()
    total_sessions = Session.query.count()
    total_mappings = MentorMapping.query.filter_by(status='active').count()
    
    # Get recent sessions
    recent_sessions = Session.query.order_by(Session.created_at.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html',
                          total_students=total_students,
                          total_mentors=total_mentors,
                          total_sessions=total_sessions,
                          total_mappings=total_mappings,
                          recent_sessions=recent_sessions)

@admin_bp.route('/users')
@login_required
def users():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    role_filter = request.args.get('role', 'all')
    
    if role_filter == 'all':
        users = User.query.filter(User.role != 'admin').all()
    else:
        users = User.query.filter_by(role=role_filter).all()
    
    return render_template('admin/users.html', users=users, role_filter=role_filter)

@admin_bp.route('/mentor-allocation', methods=['GET', 'POST'])
@login_required
def mentor_allocation():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        mentor_id = request.form.get('mentor_id')
        
        try:
            # Check if mapping already exists
            existing = MentorMapping.query.filter_by(
                student_id=student_id,
                mentor_id=mentor_id
            ).first()
            
            if existing:
                flash('This mentor is already assigned to this student', 'warning')
                return redirect(url_for('admin.mentor_allocation'))
            
            # Create mapping
            mapping = MentorMapping(
                student_id=student_id,
                mentor_id=mentor_id,
                status='active'
            )
            db.session.add(mapping)
            
            # Create notification
            notification = Notification(
                user_id=student_id,
                title='Mentor Assigned',
                message='A new mentor has been assigned to you',
                notification_type='assignment'
            )
            db.session.add(notification)
            
            db.session.commit()
            flash('Mentor assigned successfully!', 'success')
            return redirect(url_for('admin.mentor_allocation'))
        except Exception as e:
            flash(f'Error assigning mentor: {str(e)}', 'danger')
            db.session.rollback()
    
    students = User.query.filter_by(role='student').all()
    mentors = User.query.filter_by(role='mentor').all()
    mappings = MentorMapping.query.filter_by(status='active').all()
    
    return render_template('admin/mentor_allocation.html',
                          students=students,
                          mentors=mentors,
                          mappings=mappings)

@admin_bp.route('/announcements', methods=['GET', 'POST'])
@login_required
def announcements():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        target_audience = request.form.get('target_audience')
        
        try:
            announcement = Announcement(
                admin_id=current_user.user_id,
                title=title,
                message=message,
                target_audience=target_audience
            )
            db.session.add(announcement)
            db.session.commit()
            flash('Announcement created successfully!', 'success')
            return redirect(url_for('admin.announcements'))
        except Exception as e:
            flash(f'Error creating announcement: {str(e)}', 'danger')
            db.session.rollback()
    
    all_announcements = Announcement.query.order_by(
        Announcement.announcement_date.desc()
    ).all()
    
    return render_template('admin/announcements.html',
                          announcements=all_announcements)

@admin_bp.route('/analytics')
@login_required
def analytics():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    # Get feedback statistics
    feedback = Feedback.query.all()
    avg_rating = sum([f.rating for f in feedback]) / len(feedback) if feedback else 0
    
    # Get session statistics
    completed_sessions = Session.query.filter_by(status='completed').count()
    total_sessions = Session.query.count()
    
    # Get task statistics
    completed_tasks = Task.query.filter_by(status='completed').count()
    total_tasks = Task.query.count()
    
    return render_template('admin/analytics.html',
                          avg_rating=avg_rating,
                          completed_sessions=completed_sessions,
                          total_sessions=total_sessions,
                          completed_tasks=completed_tasks,
                          total_tasks=total_tasks)

@admin_bp.route('/users/<int:user_id>/approve', methods=['POST'])
@login_required
def approve_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    user = User.query.get_or_404(user_id)
    
    try:
        if user.role == 'mentor':
            mentor_profile = MentorProfile.query.get(user_id)
            if mentor_profile:
                mentor_profile.is_approved = True
                mentor_profile.approval_date = datetime.utcnow()
                db.session.commit()
                
                notification = Notification(
                    user_id=user_id,
                    title='Profile Approved',
                    message='Your mentor profile has been approved!',
                    notification_type='approval'
                )
                db.session.add(notification)
                db.session.commit()
        
        flash(f'User {user.email} approved successfully', 'success')
    except Exception as e:
        flash(f'Error approving user: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.users'))

@admin_bp.route('/users/<int:user_id>/reject', methods=['POST'])
@login_required
def reject_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    user = User.query.get_or_404(user_id)
    reason = request.form.get('reason', '')
    
    try:
        if user.role == 'mentor':
            mentor_profile = MentorProfile.query.get(user_id)
            if mentor_profile:
                mentor_profile.is_approved = False
        
        notification = Notification(
            user_id=user_id,
            title='Profile Rejected',
            message=f'Your profile has been rejected. Reason: {reason}',
            notification_type='rejection'
        )
        db.session.add(notification)
        db.session.commit()
        
        flash(f'User {user.email} rejected', 'info')
    except Exception as e:
        flash(f'Error rejecting user: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.users'))

@admin_bp.route('/users/<int:user_id>/status', methods=['POST'])
@login_required
def change_user_status(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    user = User.query.get_or_404(user_id)
    new_status = request.form.get('status')
    
    try:
        if user.role == 'mentor':
            mentor_quality = MentorQuality.query.filter_by(mentor_id=user_id).first()
            if not mentor_quality:
                mentor_quality = MentorQuality(mentor_id=user_id)
                db.session.add(mentor_quality)
            
            mentor_quality.is_active = (new_status == 'active')
            db.session.commit()
        
        flash(f'User status updated to {new_status}', 'success')
    except Exception as e:
        flash(f'Error updating status: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.users'))

@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        role = request.form.get('role')
        
        try:
            user.name = name
            user.email = email
            user.phone = phone
            if role in ['student', 'mentor']:
                user.role = role
            
            db.session.commit()
            flash(f'User {user.email} updated successfully', 'success')
            return redirect(url_for('admin.users'))
        except Exception as e:
            flash(f'Error updating user: {str(e)}', 'danger')
            db.session.rollback()
    
    return render_template('admin/edit_user.html', user=user)

@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    if user_id == current_user.user_id:
        flash('Cannot delete your own account', 'danger')
        return redirect(url_for('admin.users'))
    
    user = User.query.get_or_404(user_id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        flash(f'User {user.email} deleted successfully', 'success')
    except Exception as e:
        flash(f'Error deleting user: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.users'))

@admin_bp.route('/mentor-allocation/balance', methods=['POST'])
@login_required
def balance_workload():
    """Automatically balance mentor workload"""
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    try:
        # Get all mentors with their current mentee counts
        mentors = User.query.filter_by(role='mentor').all()
        mentors_load = {}
        
        for mentor in mentors:
            count = MentorMapping.query.filter_by(
                mentor_id=mentor.user_id,
                status='active'
            ).count()
            mentors_load[mentor.user_id] = count
        
        # Get unassigned students
        unassigned_students = db.session.query(User).outerjoin(
            MentorMapping, User.user_id == MentorMapping.student_id
        ).filter(
            User.role == 'student',
            MentorMapping.map_id.is_(None)
        ).all()
        
        # Assign to mentors with lowest workload
        for student in unassigned_students:
            min_mentor = min(mentors_load, key=mentors_load.get)
            
            mapping = MentorMapping(
                student_id=student.user_id,
                mentor_id=min_mentor,
                status='active'
            )
            db.session.add(mapping)
            mentors_load[min_mentor] += 1
        
        db.session.commit()
        flash('Workload balanced successfully', 'success')
    except Exception as e:
        flash(f'Error balancing workload: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.mentor_allocation'))

@admin_bp.route('/mentor-allocation/<int:mapping_id>/delete', methods=['POST'])
@login_required
def delete_allocation(mapping_id):
    """Delete a mentor allocation"""
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    mapping = MentorMapping.query.get_or_404(mapping_id)
    
    try:
        student = User.query.get(mapping.student_id)
        mentor = User.query.get(mapping.mentor_id)
        
        db.session.delete(mapping)
        db.session.commit()
        flash(f'Allocation between {student.name if student else "Student"} and {mentor.name if mentor else "Mentor"} removed successfully', 'success')
    except Exception as e:
        flash(f'Error removing allocation: {str(e)}', 'danger')
        db.session.rollback()
    
    return redirect(url_for('admin.mentor_allocation'))

@admin_bp.route('/mentor-allocation/<int:mapping_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_allocation(mapping_id):
    """Edit a mentor allocation"""
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    mapping = MentorMapping.query.get_or_404(mapping_id)
    
    if request.method == 'POST':
        new_mentor_id = request.form.get('mentor_id')
        new_status = request.form.get('status')
        
        try:
            mapping.mentor_id = int(new_mentor_id)
            mapping.status = new_status
            db.session.commit()
            flash('Allocation updated successfully', 'success')
            return redirect(url_for('admin.mentor_allocation'))
        except Exception as e:
            flash(f'Error updating allocation: {str(e)}', 'danger')
            db.session.rollback()
    
    students = User.query.filter_by(role='student').all()
    mentors = User.query.filter_by(role='mentor').all()
    
    return render_template('admin/edit_allocation.html', 
                          mapping=mapping, 
                          students=students, 
                          mentors=mentors)

@admin_bp.route('/quality-monitoring')
@login_required
def quality_monitoring():
    """Monitor mentor quality and performance"""
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    # Get all mentors with their quality data
    all_mentors_data = db.session.query(
        MentorQuality,
        User
    ).outerjoin(User, MentorQuality.mentor_id == User.user_id).filter(
        User.role == 'mentor'
    ).all()
    
    # Get top mentors (by rating, marked as top mentor)
    top_mentors = []
    for mq, user in all_mentors_data:
        if mq and mq.is_top_mentor:
            top_mentors.append({'quality': mq, 'user': user})
    top_mentors = sorted(top_mentors, key=lambda x: x['quality'].overall_rating if x['quality'] else 0, reverse=True)[:5]
    
    # Get inactive mentors (no session in 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    all_mentor_users = User.query.filter_by(role='mentor').all()
    
    inactive_mentors = []
    for user in all_mentor_users:
        recent_session = Session.query.filter(
            Session.mentor_id == user.user_id,
            Session.created_at >= thirty_days_ago
        ).first()
        if not recent_session:
            # Get quality data for this mentor
            mq = MentorQuality.query.filter_by(mentor_id=user.user_id).first()
            inactive_mentors.append({'user': user, 'quality': mq})
    
    # Get active mentors count
    active_mentors_count = len(all_mentor_users) - len(inactive_mentors)
    
    # Get total sessions count
    total_sessions_count = Session.query.count()
    
    # Get all feedback for average rating calculation
    all_feedback = Feedback.query.all()
    avg_mentor_rating = sum([f.rating for f in all_feedback]) / len(all_feedback) if all_feedback else 0
    
    # Calculate platform satisfaction (based on feedback)
    if all_feedback:
        positive_feedback = sum([1 for f in all_feedback if f.rating >= 4])
        platform_satisfaction = round((positive_feedback / len(all_feedback)) * 100, 1)
    else:
        platform_satisfaction = 0
    
    # Get satisfaction metrics (mentor rankings)
    satisfaction_metrics = []
    for mq, user in all_mentors_data:
        if user:
            avg_rating = db.session.query(func.avg(Feedback.rating)).filter(
                Feedback.mentor_id == user.user_id
            ).scalar() or 0
            
            session_count = Session.query.filter_by(
                mentor_id=user.user_id,
                status='completed'
            ).count()
            
            satisfaction_metrics.append({
                'mentor_name': user.name,
                'mentor_id': user.user_id,
                'avg_rating': avg_rating,
                'session_count': session_count
            })
    
    # Sort by rating descending
    satisfaction_metrics = sorted(satisfaction_metrics, key=lambda x: x['avg_rating'], reverse=True)
    
    # Legacy satisfaction_data for backwards compatibility with template
    satisfaction_data = []
    for mentor in all_mentor_users:
        avg_rating = db.session.query(func.avg(Feedback.rating)).filter(
            Feedback.mentor_id == mentor.user_id
        ).scalar() or 0
        
        session_count = Session.query.filter_by(
            mentor_id=mentor.user_id,
            status='completed'
        ).count()
        
        mq = MentorQuality.query.filter_by(mentor_id=mentor.user_id).first()
        
        satisfaction_data.append({
            'mentor': mentor,
            'rating': avg_rating,
            'sessions': session_count,
            'quality': mq
        })
    
    return render_template('admin/quality_monitoring.html',
                          top_mentors=top_mentors,
                          inactive_mentors=inactive_mentors,
                          satisfaction_data=satisfaction_data,
                          avg_mentor_rating=round(avg_mentor_rating, 2),
                          active_mentors_count=active_mentors_count,
                          total_sessions_count=total_sessions_count,
                          platform_satisfaction=platform_satisfaction,
                          satisfaction_metrics=satisfaction_metrics)

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """Platform settings management"""
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))
    
    if request.method == 'POST':
        # Check if this is adding a new setting or updating an existing one
        new_key = request.form.get('new_key')
        new_value = request.form.get('new_value')
        new_type = request.form.get('new_type')
        
        try:
            if new_key:
                # Adding a new setting
                setting_key = new_key
                setting_value = new_value
                setting_type = new_type or 'string'
                
                setting = PlatformSettings.query.filter_by(setting_key=setting_key).first()
                
                if not setting:
                    setting = PlatformSettings(
                        setting_key=setting_key,
                        setting_type=setting_type
                    )
                    db.session.add(setting)
                
                setting.setting_value = setting_value
                db.session.commit()
                flash('New setting added successfully', 'success')
            else:
                # Updating existing settings - iterate through all existing settings
                settings_list = PlatformSettings.query.all()
                for setting in settings_list:
                    form_value = request.form.get(setting.setting_key)
                    if form_value is not None:
                        setting.setting_value = form_value
                db.session.commit()
                flash('Settings updated successfully', 'success')
            
            return redirect(url_for('admin.settings'))
        except Exception as e:
            flash(f'Error saving setting: {str(e)}', 'danger')
            db.session.rollback()
    
    settings_list = PlatformSettings.query.all()
    
    return render_template('admin/settings.html', settings=settings_list)

@admin_bp.route('/sessions')
@login_required
def sessions():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))

    all_sessions = Session.query.all()

    return render_template('admin/sessions.html', sessions=all_sessions)

@admin_bp.route('/profile')
@login_required
def profile():
    if current_user.role != 'admin':
        return redirect(url_for('admin.login'))

    return render_template('admin/profile.html', user=current_user)
