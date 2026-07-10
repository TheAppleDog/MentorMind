# Admin Setup Guide - MentorMind

## Default Admin Account

The MentorMind platform comes with a default admin account for initial setup and management.

### Admin Credentials

```
Name:     Khushi Kulkarni
Email:    admin@mentormind.com
Password: Admin@123456
Role:     admin
```

## Setting Up Admin Account

### Method 1: Automatic Setup (Recommended)

Run the setup script to automatically create the admin account:

```bash
python setup_admin.py
```

This will:
- Create the admin user in the database
- Display the admin credentials
- Confirm setup success

### Method 2: Manual Setup

If you prefer to set up manually, you can use a Python shell:

```bash
# Start Python interactive shell in the project directory
python

# Then run:
import sys
sys.path.insert(0, 'backend')
from app import create_app
from app.models.models import db, User

app = create_app()
with app.app_context():
    admin = User(name='Khushi Kulkarni', email='admin@mentormind.com', role='admin')
    admin.set_password('Admin@123456')
    db.session.add(admin)
    db.session.commit()
    print("Admin created successfully!")
```

## Accessing Admin Panel

1. Start the application:
   ```bash
   python run.py
   ```

2. Navigate to: `http://localhost:5000/login`

3. Enter admin credentials:
   - **Email:** admin@mentormind.com
   - **Password:** Admin@123456

4. Access the admin dashboard at: `/admin/dashboard`

## Admin Capabilities

As an admin user, you can:

- **User Management** (`/admin/users`)
  - View all students and mentors
  - Filter by role
  - Manage user accounts

- **Dashboard** (`/admin/dashboard`)
  - View platform statistics
  - Monitor active sessions
  - Track mentor mappings
  - Review recent activity

- **Mentor Allocation** (`/admin/mentor-allocation`)
  - Assign mentors to students
  - Manage mentor-student relationships
  - Track allocation status

- **Announcements** (`/admin/announcements`)
  - Create platform-wide announcements
  - Manage notifications

- **Reports** (`/admin/reports`)
  - Generate session reports
  - View feedback analysis
  - Monitor mentor performance

- **Settings** (`/admin/settings`)
  - Configure platform settings
  - Manage feature toggles

## Important Security Notes

⚠️ **Security Best Practices:**

1. **Change Default Password**
   - Change the default password immediately after first login
   - Use a strong password with:
     - At least 8 characters
     - Mix of letters, numbers, and symbols

2. **Account Security**
   - Never share admin credentials
   - Use unique, strong passwords
   - Enable login tracking if available

3. **Backup Admin Account**
   - Keep a backup admin account for emergency access
   - Document recovery procedures

4. **Audit Trail**
   - Admin actions are logged
   - Review logs regularly for suspicious activity
   - Monitor user access patterns

## Troubleshooting

### Admin Account Already Exists
If you run `setup_admin.py` and the admin already exists:
```
✓ Admin user already exists!
  Email: admin@mentormind.com
  Name: Khushi Kulkarni
  Role: admin
```

This is normal - the script won't recreate duplicate accounts.

### Can't Login
- Verify email: `admin@mentormind.com`
- Verify password: `Admin@123456`
- Check database connection
- Ensure application is running on correct port (5000)

### Database Issues
If admin account doesn't appear:
1. Delete the database file (if using SQLite)
2. Run `python setup_admin.py` again
3. The tables will be created automatically

## File Structure

```
MentorMind/
├── setup_admin.py          # Admin setup script
├── run.py                  # Application entry point
├── backend/
│   └── app/
│       ├── models/models.py     # Database models
│       ├── routes/admin.py      # Admin routes
│       ├── routes/auth.py       # Authentication routes
│       └── templates/
│           ├── auth/login.html  # Login page with admin info
│           └── admin/           # Admin templates
└── database/
    └── mentormind.db       # SQLite database (auto-created)
```

## Admin Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/login` | GET, POST | Admin login page |
| `/admin/dashboard` | GET | Admin dashboard |
| `/admin/users` | GET | User management |
| `/admin/mentor-allocation` | GET, POST | Mentor assignment |
| `/admin/announcements` | GET, POST | Platform announcements |
| `/admin/reports` | GET | Reports and analytics |
| `/admin/settings` | GET, POST | Platform settings |

## Next Steps

1. ✅ Create admin account
2. ✅ Login to platform
3. ✅ Change default password
4. ✅ Configure platform settings
5. ✅ Create student/mentor test accounts
6. ✅ Test platform features

---

For more information, see [QUICKSTART.md](QUICKSTART.md) or [README.md](README.md)
