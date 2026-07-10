#!/usr/bin/env python3
"""
Script to set up default admin account for MentorMind
Admin Name: Khushi Kulkarni
Default Email: admin@mentormind.com
Default Password: Admin@123456
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from app.models.models import db, User

def setup_admin():
    app = create_app()
    
    with app.app_context():
        # Check if admin already exists
        admin_user = User.query.filter_by(email='admin@mentormind.com').first()
        
        if admin_user:
            print("✓ Admin user already exists!")
            print(f"  Email: {admin_user.email}")
            print(f"  Name: {admin_user.name}")
            print(f"  Role: {admin_user.role}")
            return
        
        # Create admin user
        admin = User(
            name='Khushi Kulkarni',
            email='admin@mentormind.com',
            role='admin'
        )
        admin.set_password('Admin@123456')
        
        db.session.add(admin)
        db.session.commit()
        
        print("✓ Admin account created successfully!")
        print("\n" + "="*50)
        print("ADMIN LOGIN CREDENTIALS")
        print("="*50)
        print(f"Email:    admin@mentormind.com")
        print(f"Password: Admin@123456")
        print(f"Name:     Khushi Kulkarni")
        print("="*50)
        print("\n👉 Login at: http://localhost:5000/login")
        print("\n⚠️  IMPORTANT:")
        print("   - Change the default password after first login")
        print("   - Use this account for admin dashboard access")
        print("="*50 + "\n")

if __name__ == '__main__':
    setup_admin()
