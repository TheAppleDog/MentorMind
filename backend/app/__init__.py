from flask import Flask
from flask_login import LoginManager
from .models.models import db, User
from .routes.auth import auth_bp
from .routes.student import student_bp
from .routes.mentor import mentor_bp
from .routes.admin import admin_bp
import os
import sys

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from config.config import config

login_manager = LoginManager()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(mentor_bp, url_prefix='/mentor')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Create database tables and initialize admin
    with app.app_context():
        db.create_all()
        
        # Create default admin account if it doesn't exist
        admin_user = User.query.filter_by(email='admin@mentormind.com').first()
        if not admin_user:
            admin = User(
                name='Khushi Kulkarni',
                email='admin@mentormind.com',
                role='admin'
            )
            admin.set_password('Admin@123456')
            db.session.add(admin)
            db.session.commit()
            print("\n" + "="*60)
            print("✓ DEFAULT ADMIN ACCOUNT CREATED")
            print("="*60)
            print("Name:     Khushi Kulkarni")
            print("Email:    admin@mentormind.com")
            print("Password: Admin@123456")
            print("="*60)
            print("⚠️  IMPORTANT: Change the password after first login!")
            print("="*60 + "\n")
    
    return app

