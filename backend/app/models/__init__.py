from .models import db, User

def init_db():
    """Initialize the database"""
    db.create_all()
    print("Database initialized successfully!")

def create_admin(name, email, password):
    """Create an admin user"""
    admin = User(name=name, email=email, role='admin')
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    print(f"Admin user '{email}' created successfully!")

def seed_data():
    """Seed sample data for testing"""
    # This function can be used to populate test data
    pass
