import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app

app = create_app()

with app.app_context():
    from app.models.models import db, Announcement, User

    admin = User.query.filter_by(email='admin@mentormind.com').first()

    if admin:
        announcements = [
            {
                'title': 'Welcome to MentorMind!',
                'message': 'We are excited to have you join our mentoring platform. Get started by exploring your dashboard and connecting with mentors.',
                'target_audience': 'all'
            },
            {
                'title': 'New Feature: Session Scheduling',
                'message': 'You can now schedule mentoring sessions directly through the platform. Check your dashboard for available slots.',
                'target_audience': 'students'
            },
            {
                'title': 'Mentor Training Program',
                'message': 'All mentors are required to complete the online training module. Access it from your profile page.',
                'target_audience': 'mentors'
            },
            {
                'title': 'Platform Maintenance Notice',
                'message': 'The platform will be undergoing maintenance on Sunday from 2 AM to 4 AM. Please plan accordingly.',
                'target_audience': 'all'
            },
            {
                'title': 'Student Progress Tracking',
                'message': 'New progress tracking features are now available. Monitor your learning journey and achievements.',
                'target_audience': 'students'
            }
        ]

        for ann in announcements:
            announcement = Announcement(
                admin_id=admin.user_id,
                title=ann['title'],
                message=ann['message'],
                target_audience=ann['target_audience']
            )
            db.session.add(announcement)

        db.session.commit()
        print("5 announcements added successfully!")
    else:
        print("Admin user not found!")
