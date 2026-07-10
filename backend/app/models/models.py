from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # student, mentor, admin
    phone = db.Column(db.String(15))
    profile_picture = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    student_profile = db.relationship('StudentProfile', backref='user', uselist=False)
    mentor_profile = db.relationship('MentorProfile', backref='user', uselist=False)
    
    def get_id(self):
        return self.user_id
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'
    
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    academic_level = db.Column(db.String(50))
    interests = db.Column(db.Text)
    career_goals = db.Column(db.Text)
    skills = db.Column(db.Text)
    gpa = db.Column(db.Float)
    major = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MentorProfile(db.Model):
    __tablename__ = 'mentor_profiles'
    
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    expertise = db.Column(db.Text, nullable=False)
    experience_years = db.Column(db.Integer)
    specialization = db.Column(db.String(100))
    bio = db.Column(db.Text)
    professional_title = db.Column(db.String(100))
    organization = db.Column(db.String(200))
    certifications = db.Column(db.Text)  # Comma-separated
    availability_hours = db.Column(db.JSON)  # {day: [start_time, end_time]}
    hourly_rate = db.Column(db.Float)
    max_mentees = db.Column(db.Integer, default=5)
    current_mentees = db.Column(db.Integer, default=0)
    is_approved = db.Column(db.Boolean, default=False)
    approval_date = db.Column(db.DateTime)
    average_rating = db.Column(db.Float, default=0.0)
    total_sessions = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MentorMapping(db.Model):
    __tablename__ = 'mentor_mapping'
    
    map_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    assigned_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # active, inactive, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Session(db.Model):
    __tablename__ = 'sessions'
    
    session_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.Time, nullable=False)
    duration_minutes = db.Column(db.Integer, default=60)
    topic = db.Column(db.String(255))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, approved, rejected, completed, cancelled, rescheduled
    approval_status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    notes = db.Column(db.Text)
    mentor_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

class Task(db.Model):
    __tablename__ = 'tasks'
    
    task_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.Date)
    status = db.Column(db.String(20), default='pending')  # pending, in-progress, completed
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    progress_percentage = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SkillTracking(db.Model):
    __tablename__ = 'skill_tracking'
    
    skill_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), default='beginner')  # beginner, intermediate, advanced, expert
    proficiency_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    feedback_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.session_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    rating = db.Column(db.Integer)  # 1-5
    comment = db.Column(db.Text)
    suggestion = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Milestone(db.Model):
    __tablename__ = 'milestones'
    
    milestone_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    target_date = db.Column(db.Date)
    achieved_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='pending')  # pending, achieved
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Announcement(db.Model):
    __tablename__ = 'announcements'
    
    announcement_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    announcement_date = db.Column(db.DateTime, default=datetime.utcnow)
    target_audience = db.Column(db.String(20), default='all')  # students, mentors, all
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CareerRoadmap(db.Model):
    __tablename__ = 'career_roadmap'
    
    roadmap_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    current_stage = db.Column(db.String(100))
    next_stage = db.Column(db.String(100))
    suggested_certifications = db.Column(db.Text)
    internship_readiness = db.Column(db.String(50))
    placement_stage = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(50))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SessionNotes(db.Model):
    __tablename__ = 'session_notes'
    
    note_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.session_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    key_points = db.Column(db.JSON)  # List of key discussion points
    student_progress = db.Column(db.String(50))  # Good, Fair, Poor
    next_focus_areas = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MentorQuality(db.Model):
    __tablename__ = 'mentor_quality'
    
    quality_id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    overall_rating = db.Column(db.Float, default=0.0)
    session_count = db.Column(db.Integer, default=0)
    completion_rate = db.Column(db.Float, default=0.0)
    student_satisfaction = db.Column(db.Float, default=0.0)
    response_time_hours = db.Column(db.Float)
    last_active = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    is_top_mentor = db.Column(db.Boolean, default=False)
    flags = db.Column(db.JSON)  # Any issues or flags
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PlatformSettings(db.Model):
    __tablename__ = 'platform_settings'
    
    setting_id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100), unique=True, nullable=False)
    setting_value = db.Column(db.Text)
    setting_type = db.Column(db.String(20))  # int, string, bool, json
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class RiskAlert(db.Model):
    __tablename__ = 'risk_alerts'
    
    alert_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    risk_level = db.Column(db.String(20), default='low')  # low, medium, high, critical
    status = db.Column(db.String(20), default='active')  # active, resolved, dismissed
    
    # Performance metrics
    session_attendance_rate = db.Column(db.Float, default=100.0)  # Percentage of attended sessions
    task_completion_rate = db.Column(db.Float, default=100.0)  # Percentage of completed tasks
    avg_feedback_score = db.Column(db.Float, default=5.0)  # Average feedback rating (1-5)
    progress_rate = db.Column(db.Float, default=100.0)  # Overall progress percentage
    
    # Risk factors (JSON array of strings)
    risk_factors = db.Column(db.JSON)  # e.g., ["low_attendance", "missed_deadlines", "poor_feedback"]
    
    # Recommendations
    recommendations = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    
    # Relationships
    student = db.relationship('User', foreign_keys=[student_id], backref='risk_alerts')
    mentor = db.relationship('User', foreign_keys=[mentor_id])
