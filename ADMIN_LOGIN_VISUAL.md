# Admin Login - Visual Guide

## 🎯 Where is Admin Login?

The admin login is displayed on the **regular login page** at the bottom.

### Login Page Location
```
URL: http://localhost:5000/login
File: backend/app/templates/auth/login.html
```

### What You'll See

```
┌─────────────────────────────────────────────────────┐
│           MentorMind Login Page                      │
│                                                     │
│              🧠 Welcome Back                        │
│         Sign in to your MentorMind account          │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │ 📧 Email Address                            │   │
│  │ [_________________________________]         │   │
│  │                                             │   │
│  │ 🔐 Password                                 │   │
│  │ [_________________________________] 👁️     │   │
│  │                                             │   │
│  │ ☑️ Remember me    [Forgot password?]       │   │
│  │                                             │   │
│  │  [✓ Sign In]                                │   │
│  │                                             │   │
│  │  ─────────── or ───────────                 │   │
│  │                                             │   │
│  │  Don't have an account?                     │   │
│  │  [→ Create one here]                        │   │
│  │                                             │   │
│  │  ┌───────────────────────────────────────┐  │   │
│  │  │ 🛡️  Admin Login                        │  │   │
│  │  │ Email:     admin@mentormind.com        │  │   │
│  │  │ Password:  Admin@123456                │  │   │
│  │  │ Admin Name: Khushi Kulkarni            │  │   │
│  │  └───────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## 📋 Admin Login Information Box

Located at the **bottom of the login form**, this box displays:

```
┌─────────────────────────────────────────────┐
│          🛡️  Admin Login                     │
├─────────────────────────────────────────────┤
│                                             │
│  Email:         admin@mentormind.com        │
│  Password:      Admin@123456                │
│  Admin Name:    Khushi Kulkarni             │
│                                             │
└─────────────────────────────────────────────┘
```

**Styling:**
- Light blue background (rgba(99, 102, 241, 0.05))
- Blue border (rgba(99, 102, 241, 0.2))
- Rounded corners (10px)
- Small text (0.75rem)
- Icon: Shield (🛡️)

## 🔐 Login Credentials

```
┌────────────────────────────────────────┐
│        DEFAULT ADMIN CREDENTIALS       │
├────────────────────────────────────────┤
│                                        │
│  Name:         Khushi Kulkarni         │
│  Email:        admin@mentormind.com    │
│  Password:     Admin@123456            │
│  Role:         Administrator           │
│  Status:       Active                  │
│                                        │
│  Login URL:    http://localhost:5000/  │
│                       login            │
│                                        │
│  Dashboard:    http://localhost:5000/  │
│                       admin/dashboard  │
│                                        │
└────────────────────────────────────────┘
```

## 🖱️ How to Login as Admin

### Step 1: Visit Login Page
```
Browser URL Bar: http://localhost:5000/login
Press Enter →
```

### Step 2: Locate Admin Login Info
```
The login form appears with:
- Email input field
- Password input field
- Sign In button

Below that you'll see:
- Registration link
- "Admin Login" information box ← HERE
```

### Step 3: Copy Admin Credentials
```
From the Admin Login box, copy:

Email:    admin@mentormind.com
Password: Admin@123456
```

### Step 4: Enter Email
```
Click Email input field →
Paste: admin@mentormind.com →
```

### Step 5: Enter Password
```
Click Password input field →
Paste: Admin@123456 →
(Use eye icon to verify if needed)
```

### Step 6: Click Sign In
```
Click the blue "Sign In" button →

Result:
- Confetti animation plays
- Redirected to: http://localhost:5000/admin/dashboard
```

## 📊 Admin Dashboard

After login, you'll see:

```
┌─────────────────────────────────────────────────┐
│  MentorMind Admin Dashboard                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  📊 STATISTICS                                  │
│  ├─ Total Students: 42                         │
│  ├─ Total Mentors: 18                          │
│  ├─ Total Sessions: 156                        │
│  └─ Active Mappings: 38                        │
│                                                 │
│  📋 MENU                                        │
│  ├─ Users        (/admin/users)               │
│  ├─ Mentor Allocation                          │
│  ├─ Announcements                              │
│  ├─ Reports                                    │
│  └─ Settings                                   │
│                                                 │
│  📅 RECENT SESSIONS                             │
│  ├─ Session 1: John Doe & Jane Smith ...       │
│  ├─ Session 2: Alice Johnson & Bob Wilson ...  │
│  └─ More sessions...                           │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 🔍 Finding Admin Login Info

**If you can't find the Admin Login box:**

1. Open login page: `http://localhost:5000/login`
2. Look for the sign-in form
3. **Scroll down** ↓ (important!)
4. Below "Create one here" link
5. You'll see the blue "Admin Login" box

## 🎨 Admin Login Box Design

```
┌─────────────────────────────────────────┐  ← Rounded corner (border-radius: 10px)
│ 🛡️  Admin Login                          │  ← Icon + Title (font-size: 0.85rem)
├─────────────────────────────────────────┤  ← Light divider
│ Email:     admin@mentormind.com         │  ← Bold labels, regular values
│ Password:  Admin@123456                 │  ← All text: font-size: 0.75rem
│ Admin Name: Khushi Kulkarni             │  ← Color: text-muted (#6c757d)
└─────────────────────────────────────────┘  ← Rounded corner

Background: rgba(99, 102, 241, 0.05)  ← Light blue
Border:     rgba(99, 102, 241, 0.2)   ← Darker blue
Padding:    12px
Margin:     margin-top: 1rem
```

## 📱 Responsive Design

### Desktop (Large Screen)
```
┌─────────────────────────────────────────┐
│         Login Form (500px)              │
│                                         │
│    Email & Password fields              │
│    Sign In button                       │
│    Or divider                           │
│    Register link                        │
│    Admin Login Info Box ← Shows here    │
│                                         │
│    Footer                               │
└─────────────────────────────────────────┘
```

### Tablet (Medium Screen)
```
┌───────────────────────────────────┐
│   Login Form (Medium)             │
│                                   │
│   All elements stack properly      │
│   Admin box remains visible        │
│                                   │
└───────────────────────────────────┘
```

### Mobile (Small Screen)
```
┌──────────────┐
│ Login Form   │
│              │
│ Email        │
│ Password     │
│ Sign In      │
│ Or           │
│ Register     │
│ Admin Info ← Shows properly
│              │
└──────────────┘
```

## ✨ Key Features

✓ **Always Visible** - Admin credentials displayed on login page
✓ **Easy Access** - Just scroll down to see
✓ **Clear Layout** - Organized in info box
✓ **Styled** - Matches MentorMind design system
✓ **Responsive** - Works on all screen sizes
✓ **Secure** - Only displayed on login page for reference

## 🔒 Security Notes

⚠️ **The credentials are shown on the login page for:**
- Setup and configuration
- New admin testing
- Development/demo purposes

🛡️ **In production, you should:**
- Change the default password
- Remove the info box (optional)
- Use environment variables for admin setup
- Implement 2FA (two-factor authentication)
- Monitor admin access logs

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't see Admin Login box | Scroll down the login page |
| Box is cut off | Check browser zoom (100%) |
| Can't copy credentials | The box text is selectable, try triple-click |
| Missing from login page | Refresh browser cache (Ctrl+F5) |

## 📸 Screenshot Path

The admin login info box is located at:
- **File:** `backend/app/templates/auth/login.html`
- **Lines:** ~82-90 (the Admin Login info section)
- **CSS:** Inline styles in the div

## 🎯 Quick Access

```
Login Page:     http://localhost:5000/login
Dashboard:      http://localhost:5000/admin/dashboard
Users:          http://localhost:5000/admin/users
Announcements:  http://localhost:5000/admin/announcements
Settings:       http://localhost:5000/admin/settings
```

---

**Admin Setup:** ✅ Complete
**Admin Name:** Khushi Kulkarni
**Status:** Ready to use
