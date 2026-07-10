# Admin Account Setup - Summary

## 🔐 Default Admin Credentials

```
┌─────────────────────────────────────────┐
│         ADMIN LOGIN CREDENTIALS         │
├─────────────────────────────────────────┤
│ Name:     Khushi Kulkarni               │
│ Email:    admin@mentormind.com          │
│ Password: Admin@123456                  │
│ Role:     Administrator                 │
└─────────────────────────────────────────┘
```

## 📍 Admin Login Location

The admin login is **on the same login page as regular users and mentors**.

- **URL:** `http://localhost:5000/login`
- **Page:** [backend/app/templates/auth/login.html](backend/app/templates/auth/login.html)
- **Credentials Display:** Admin credentials are displayed on the login page under an "Admin Login" information box

## ⚙️ How Admin Setup Works

### Automatic Setup (On App Start)
When you run `python run.py`:
1. The app initializes the database
2. Checks if admin account exists
3. If NOT found, automatically creates:
   - Email: admin@mentormind.com
   - Name: Khushi Kulkarni
   - Password: Admin@123456 (hashed)
4. Prints confirmation message to console

### Manual Setup Option
If needed, run:
```bash
python setup_admin.py
```

This script:
- Checks if admin already exists
- Creates admin if not found
- Displays login credentials
- Shows secure setup confirmation

## 🎯 What Admin Can Access

After logging in with admin credentials, access:

1. **Admin Dashboard** → `/admin/dashboard`
   - Platform statistics
   - Recent activity
   - User counts
   - Session monitoring

2. **User Management** → `/admin/users`
   - View all students
   - View all mentors
   - Filter by role
   - Manage accounts

3. **Mentor Allocation** → `/admin/mentor-allocation`
   - Assign mentors to students
   - Manage relationships
   - Track allocations

4. **Announcements** → `/admin/announcements`
   - Create notifications
   - Platform-wide messages
   - Send bulk communications

5. **Reports** → `/admin/reports`
   - Generate analytics
   - Performance metrics
   - Feedback analysis

6. **Settings** → `/admin/settings`
   - Configure platform
   - Feature toggles
   - System preferences

## 📁 Files Modified/Created

### New Files
- ✅ [setup_admin.py](setup_admin.py) - Setup script
- ✅ [ADMIN_SETUP.md](ADMIN_SETUP.md) - Detailed guide

### Modified Files
- ✅ [backend/app/__init__.py](backend/app/__init__.py) - Auto-creates admin on startup
- ✅ [backend/app/templates/auth/login.html](backend/app/templates/auth/login.html) - Shows admin credentials

## 🚀 Getting Started

### Step 1: Start the Application
```bash
cd e:\MentorMind
python run.py
```

You'll see:
```
============================================================
✓ DEFAULT ADMIN ACCOUNT CREATED
============================================================
Name:     Khushi Kulkarni
Email:    admin@mentormind.com
Password: Admin@123456
============================================================
⚠️  IMPORTANT: Change the password after first login!
============================================================
```

### Step 2: Login
1. Open browser: `http://localhost:5000/login`
2. Enter credentials:
   - Email: `admin@mentormind.com`
   - Password: `Admin@123456`
3. Click "Sign In"

### Step 3: Access Admin Dashboard
- Redirects to: `/admin/dashboard`
- View platform statistics
- Manage users and settings

## ⚠️ Security Reminders

1. **Change Password** - After first login, change the default password
2. **Keep Secret** - Don't share admin credentials
3. **Use Strong Password** - When changing, use 8+ chars with symbols
4. **Backup Account** - Consider creating a backup admin account
5. **Monitor Access** - Review admin action logs regularly

## 🔗 Related Files

- **Login Page:** [backend/app/templates/auth/login.html](backend/app/templates/auth/login.html)
- **Auth Routes:** [backend/app/routes/auth.py](backend/app/routes/auth.py)
- **Admin Routes:** [backend/app/routes/admin.py](backend/app/routes/admin.py)
- **User Model:** [backend/app/models/models.py](backend/app/models/models.py)
- **Setup Script:** [setup_admin.py](setup_admin.py)
- **Detailed Guide:** [ADMIN_SETUP.md](ADMIN_SETUP.md)

## 💡 Troubleshooting

### Admin Already Exists
If running `setup_admin.py` shows "Admin user already exists", that's normal and means:
- Admin account was already created
- Database is properly configured
- You can proceed to login

### Can't Login?
- Verify exact credentials (case-sensitive for email)
- Check if server is running on port 5000
- Clear browser cache/cookies
- Check console for error messages

### Password Reset
If you forget the admin password:
1. Delete the SQLite database file
2. Restart the app to recreate with default credentials
3. Or run `setup_admin.py` on a fresh database

---

**For more details, see:** [ADMIN_SETUP.md](ADMIN_SETUP.md)
