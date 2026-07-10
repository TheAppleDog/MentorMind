# Admin Account - Step by Step Guide

## Where is Admin Login?

**Admin login is on the SAME login page as regular users**

- URL: `http://localhost:5000/login`
- File: `backend/app/templates/auth/login.html`
- The login page displays admin credentials for reference

## Step 1: Start the Application

```bash
cd e:\MentorMind
python run.py
```

**Expected Output:**
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

If you see this, the admin account was just created automatically.

## Step 2: Open Login Page

Open your browser and go to:
```
http://localhost:5000/login
```

You'll see a login form with:
- Email input field
- Password input field
- Password visibility toggle
- Sign In button

**Below the form, you'll see an "Admin Login" information box displaying:**
```
Admin Login
Email:     admin@mentormind.com
Password:  Admin@123456
Admin Name: Khushi Kulkarni
```

## Step 3: Enter Admin Credentials

In the login form, enter:

**Email Field:**
```
admin@mentormind.com
```

**Password Field:**
```
Admin@123456
```

Make sure:
- Email is exactly: `admin@mentormind.com` (lowercase)
- Password is exactly: `Admin@123456` (capital A, rest lowercase)
- Password visibility toggle can help verify you typed it correctly

## Step 4: Click "Sign In"

Click the blue "Sign In" button with the icon.

The page will:
- Process your login
- Validate credentials
- Display confetti animation (success!)
- Redirect to admin dashboard

## Step 5: Access Admin Dashboard

After successful login, you'll be redirected to:
```
http://localhost:5000/admin/dashboard
```

Here you can see:
- Platform statistics (total users, sessions, etc.)
- Recent sessions list
- Active mentor mappings
- Navigation menu for other admin features

## Admin Menu Options

From the admin dashboard, access:

1. **Users** (`/admin/users`)
   - View all students and mentors
   - Filter by role
   - Manage accounts

2. **Mentor Allocation** (`/admin/mentor-allocation`)
   - Assign mentors to students
   - Track relationships
   - Update allocations

3. **Announcements** (`/admin/announcements`)
   - Create notifications
   - Send messages to all users
   - Schedule announcements

4. **Reports** (`/admin/reports`)
   - Generate analytics
   - View performance metrics
   - Download reports

5. **Settings** (`/admin/settings`)
   - Configure platform
   - Manage features
   - Update preferences

## Video of Login Process

1. Open browser → http://localhost:5000/login
2. Scroll to admin login info box (it's on the login page!)
3. Copy email: admin@mentormind.com
4. Paste into Email field
5. Copy password: Admin@123456
6. Paste into Password field
7. Click Sign In button
8. See confetti animation
9. Redirected to /admin/dashboard

## Troubleshooting

### "Invalid Email or Password" Error
- Check for typos in email (should be all lowercase)
- Verify password capitalization (Admin@123456)
- Make sure you're in the right input field
- Try clearing the field and re-entering

### "Page not found" at /admin/dashboard
- Make sure you're logged in as admin
- Check that app is running (http://localhost:5000 works)
- Refresh the page
- Check browser console for errors

### Can't see Admin Login Info Box
- Scroll down on the login page
- The info box is below the "Create one here" registration link
- Check browser zoom level (should be 100%)
- Check if JavaScript is enabled

## Admin Account Details Summary

```
┌──────────────────────────────────────┐
│        KHUSHI KULKARNI - ADMIN       │
├──────────────────────────────────────┤
│ Email:    admin@mentormind.com       │
│ Password: Admin@123456               │
│ Role:     Administrator              │
│ Status:   Active                     │
│ Created:  Automatically on startup   │
└──────────────────────────────────────┘
```

## What Happens When Admin Logs In?

1. Credentials are validated against database
2. Flask-Login session is created
3. User role is verified as "admin"
4. Redirected to `/admin/dashboard`
5. Can access all admin routes
6. Admin menu appears in navbar

## Security After Login

⚠️ **IMPORTANT:**

After you successfully login with default credentials:

1. **Change the Password**
   - Go to Settings
   - Update password
   - Use strong password (8+ chars, mixed case, numbers, symbols)

2. **Create Additional Admin Accounts**
   - For backup/redundancy
   - For different team members
   - Using the Users management page

3. **Keep Credentials Secure**
   - Don't share with unauthorized users
   - Store in secure password manager
   - Remove from this file after first use

4. **Monitor Admin Access**
   - Review admin action logs
   - Check login history
   - Verify all admin activities

## Files That Set Up Admin

1. **backend/app/__init__.py**
   - Creates admin account automatically
   - Runs on every app startup
   - Creates if doesn't exist

2. **setup_admin.py**
   - Manual setup script
   - Can run anytime
   - Checks if already exists

3. **backend/app/templates/auth/login.html**
   - Displays admin credentials
   - Shows on login page
   - For reference/setup

## Related Documentation

- [ADMIN_SETUP.md](ADMIN_SETUP.md) - Detailed setup guide
- [ADMIN_LOGIN_INFO.md](ADMIN_LOGIN_INFO.md) - Summary info
- [ADMIN_CREDENTIALS.txt](ADMIN_CREDENTIALS.txt) - Quick reference
- [README.md](README.md) - Project overview

---

**Quick Link:** Admin Login → http://localhost:5000/login
**Admin Name:** Khushi Kulkarni
**Status:** ✓ Ready to use
