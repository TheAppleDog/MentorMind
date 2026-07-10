# MentorMind - Quick Start Guide

## Getting Started in 5 Minutes

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Set Up Database
```bash
# MySQL
mysql -u root -p
CREATE DATABASE mentormind;
USE mentormind;
SOURCE ..\database\schema.sql;

# Or SQLite (for development)
# Database will be created automatically
```

### 3. Configure Environment
Copy `.env` file and update if needed:
```bash
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@localhost/mentormind
```

### 4. Run Application
```bash
python run.py
```

### 5. Access Application
Open browser and go to: **http://localhost:5000**

## Default User Roles

### Registration Types
- **Student** - Access student dashboard and features
- **Mentor** - Access mentor dashboard and manage students
- **Admin** - Access admin panel (create manually or via DB)

## Quick Features Overview

### 📚 Student Dashboard
- View assigned mentor
- Schedule mentoring sessions
- Track progress and tasks
- Submit feedback
- View career roadmap

### 👨‍🏫 Mentor Dashboard
- Manage your mentees
- Schedule sessions
- Assign tasks
- View student feedback
- Monitor progress

### ⚙️ Admin Dashboard
- Manage all users
- Allocate mentors to students
- Post announcements
- View system analytics
- Monitor sessions

## Database Tables

The system includes these main tables:
- **users** - All user accounts
- **mentor_mapping** - Student-mentor pairs
- **sessions** - Mentoring meetings
- **tasks** - Goals and assignments
- **feedback** - Session ratings
- **announcements** - System messages
- Plus many more supporting tables

## File Structure

```
backend/
├── app/
│   ├── models/ → Database models
│   ├── routes/ → API endpoints
│   └── templates/ → HTML pages
├── requirements.txt → Dependencies
└── __init__.py → App initialization

frontend/
├── static/
│   ├── css/ → Stylesheets
│   └── js/ → JavaScript files
└── pages/ → HTML pages

database/
└── schema.sql → Database schema

config/
└── config.py → Settings
```

## Useful Commands

```bash
# Activate virtual environment
venv\Scripts\activate

# Install new package
pip install package_name

# Run app with debug mode
python run.py

# Access Flask shell
python -c "from app import create_app; app = create_app(); print(app)"
```

## Next Steps

1. Create an admin user in database
2. Register as student or mentor
3. Admin allocates mentors to students
4. Schedule and manage sessions
5. Track progress and provide feedback

## Customization

Edit these files to customize:
- `config/config.py` - App settings
- `backend/app/templates/` - UI pages
- `frontend/static/css/style.css` - Styling
- Database schema in `database/schema.sql`

## Security Notes

- Change `SECRET_KEY` in production
- Use strong database password
- Enable HTTPS in production
- Validate all user input
- Use environment variables for sensitive data

---

Happy Mentoring! 🎓
