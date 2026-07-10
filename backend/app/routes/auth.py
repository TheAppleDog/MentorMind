from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from ..models.models import db, User, StudentProfile, MentorProfile
from email_validator import validate_email, EmailNotValidError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            role = request.form.get('role')  # student, mentor
            
            # Validate input
            if not all([name, email, password, confirm_password, role]):
                flash('All fields are required', 'danger')
                return redirect(url_for('auth.register'))
            
            if password != confirm_password:
                flash('Passwords do not match', 'danger')
                return redirect(url_for('auth.register'))
            
            if len(password) < 6:
                flash('Password must be at least 6 characters', 'danger')
                return redirect(url_for('auth.register'))
            
            # Validate email
            valid = validate_email(email)
            email = valid.email
            
            # Check if user exists
            if User.query.filter_by(email=email).first():
                flash('Email already registered', 'danger')
                return redirect(url_for('auth.register'))
            
            # Create new user
            user = User(name=name, email=email, role=role)
            user.set_password(password)
            
            db.session.add(user)
            db.session.flush()
            
            # Create role-specific profile
            if role == 'student':
                student_profile = StudentProfile(student_id=user.user_id)
                db.session.add(student_profile)
            elif role == 'mentor':
                mentor_profile = MentorProfile(mentor_id=user.user_id)
                db.session.add(mentor_profile)
            
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
            
        except EmailNotValidError:
            flash('Invalid email address', 'danger')
            return redirect(url_for('auth.register'))
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'danger')
            db.session.rollback()
            return redirect(url_for('auth.register'))
    
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user, remember=request.form.get('remember'))
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'student':
        return redirect(url_for('student.dashboard'))
    elif current_user.role == 'mentor':
        return redirect(url_for('mentor.dashboard'))
    elif current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return redirect(url_for('auth.login'))
