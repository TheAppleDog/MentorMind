# MentorMind - Development Guide

## Architecture Overview

MentorMind follows the **Model-View-Controller (MVC)** pattern:

```
User Request
    ↓
Routes (Controller) → Models (Data) → Templates (View)
    ↓
Response to User
```

## Codebase Organization

### Backend Structure

```
app/
├── __init__.py          # App factory and initialization
├── models/
│   └── models.py        # SQLAlchemy ORM models
├── routes/
│   ├── auth.py          # Authentication (login, register, logout)
│   ├── student.py       # Student endpoints
│   ├── mentor.py        # Mentor endpoints
│   └── admin.py         # Admin endpoints
└── templates/           # Jinja2 HTML templates
    ├── base.html        # Base template (extends to all pages)
    ├── auth/            # Auth pages (login, register)
    ├── student/         # Student pages (dashboard, sessions, etc.)
    ├── mentor/          # Mentor pages
    └── admin/           # Admin pages
```

## Database Models

### User Model
```python
class User(UserMixin, db.Model):
    user_id         # Primary key
    name            # User full name
    email           # Unique email
    password_hash   # Hashed password
    role            # student/mentor/admin
    phone           # Optional phone
    profile_picture # Avatar URL
```

### Key Relationships
- **User** ↔ **StudentProfile** (1:1)
- **User** ↔ **MentorProfile** (1:1)
- **User** ↔ **MentorMapping** (1:N) - Student can have many mentors
- **Session** ↔ **Feedback** (1:N) - One session can have feedback
- **Task** ↔ **Progress** tracking through percentage field

## Creating New Features

### Adding a New Route

1. **Create route in** `routes/module.py`:
```python
@module_bp.route('/new-feature', methods=['GET', 'POST'])
@login_required
def new_feature():
    if request.method == 'POST':
        # Handle form submission
        return redirect(url_for('module.success'))
    return render_template('module/new_feature.html')
```

2. **Register blueprint in** `__init__.py`:
```python
from routes.module import module_bp
app.register_blueprint(module_bp, url_prefix='/module')
```

3. **Create template** `templates/module/new_feature.html`:
```html
{% extends "base.html" %}
{% block content %}
<!-- Page content -->
{% endblock %}
```

### Adding a New Database Model

1. **Define model in** `models/models.py`:
```python
class NewModel(db.Model):
    __tablename__ = 'new_table'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

2. **Create database table**:
```bash
# From Python shell
from app import create_app
from app.models import db

app = create_app()
with app.app_context():
    db.create_all()
```

## Template Inheritance

All templates extend `base.html`:

```html
{% extends "base.html" %}

{% block title %}Page Title - MentorMind{% endblock %}

{% block content %}
<!-- Page specific content -->
{% endblock %}

{% block extra_css %}
<!-- Additional stylesheets -->
{% endblock %}

{% block extra_js %}
<!-- Additional scripts -->
{% endblock %}
```

## Authentication Flow

```
1. User submits login form
   ↓
2. Route handler validates credentials
   ↓
3. If valid, login_user() is called
   ↓
4. Session is created with user ID
   ↓
5. User is redirected to dashboard
   ↓
6. @login_required decorator protects routes
```

## Working with Forms

### Using Flask-WTF

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process form
        pass
    return render_template('login.html', form=form)
```

## Database Queries

### Common Patterns

```python
# Get single record
user = User.query.get(user_id)
user = User.query.filter_by(email=email).first()

# Get multiple records
all_users = User.query.all()
students = User.query.filter_by(role='student').all()

# Count records
count = User.query.count()
active_count = User.query.filter_by(role='student').count()

# Update record
user.name = "New Name"
db.session.commit()

# Delete record
db.session.delete(user)
db.session.commit()

# Join queries
sessions = Session.query.join(User).filter(
    User.role == 'student'
).all()

# Pagination
page = User.query.paginate(page=1, per_page=10)
```

## Error Handling

```python
from flask import abort, render_template

# Abort with status code
if not user:
    abort(404)

# Custom error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
```

## Flash Messages

```python
from flask import flash

# Set flash message
flash('Success message', 'success')
flash('Error message', 'danger')

# In template
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <div class="alert alert-{{ category }}">
            {{ message }}
        </div>
    {% endfor %}
{% endwith %}
```

## Working with Static Files

```html
<!-- CSS -->
<link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">

<!-- JavaScript -->
<script src="{{ url_for('static', filename='js/main.js') }}"></script>

<!-- Images -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

## Frontend JavaScript Utilities

Available in `main.js`:

```javascript
// Format dates
MentorMind.formatDate(new Date())

// Calculate progress
MentorMind.calculateProgress(completed, total)

// Validate email
MentorMind.validateEmail(email)

// Filter table
MentorMind.filterTable('tableId', 'search term')

// Show toast notification
MentorMind.showToast('Message', 'info')

// AJAX request
MentorMind.makeRequest('GET', '/api/data', null, callback)
```

## Debugging

### Enable Debug Mode
```python
app.run(debug=True)
```

### Print to Console
```python
print('Debug info:', variable)
```

### Use Flask Shell
```bash
flask shell
>>> from app.models import User
>>> User.query.all()
```

### Check Database
```sql
SELECT * FROM users;
DESCRIBE sessions;
```

## Code Style Guidelines

### Python
```python
# Function naming
def get_user_sessions(user_id):
    pass

# Variable naming
student_name = "John"
session_count = 5

# Imports
from flask import Flask, render_template
from models import User, Session
```

### HTML/Templates
```html
<!-- Use semantic HTML -->
<header>Navigation</header>
<main>Content</main>
<footer>Footer</footer>

<!-- Bootstrap utilities -->
<div class="container">
<div class="row">
<div class="col-md-6">
```

### CSS
```css
/* Use variables for colors */
:root {
    --primary-color: #007bff;
}

/* Meaningful class names -->
.student-card { }
.mentor-list { }

/* Mobile-first responsive design */
@media (max-width: 768px) { }
```

## Testing

### Manual Testing
1. Register accounts with different roles
2. Test each user role's features
3. Test edge cases (empty fields, invalid data)
4. Test navigation between pages
5. Test database operations

### Testing Routes
```python
def test_login(client):
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
```

## Performance Tips

1. **Use indexes** on frequently searched columns
2. **Eager load** relationships to avoid N+1 queries
3. **Paginate** large datasets
4. **Cache** frequently accessed data
5. **Minify** CSS and JavaScript
6. **Optimize** database queries with EXPLAIN

## Security Best Practices

1. **Hash passwords** - Never store plain passwords
2. **Validate input** - Check all user inputs
3. **Use HTTPS** - Enable in production
4. **CSRF protection** - Use Flask-WTF
5. **SQL injection** - Use ORM/parameterized queries
6. **XSS prevention** - Escape template variables
7. **Secure cookies** - Use secure flags

## Deployment Checklist

- [ ] Set `DEBUG = False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Enable HTTPS
- [ ] Set up error logging
- [ ] Configure email for notifications
- [ ] Optimize static files
- [ ] Set up database backups
- [ ] Configure monitoring
- [ ] Test all features

## Common Issues & Solutions

### Issue: ModuleNotFoundError
```bash
# Solution: Activate virtual environment and install packages
pip install -r requirements.txt
```

### Issue: Database locked
```bash
# Solution: Close other connections and restart Flask
# Or use SQLite WAL mode
```

### Issue: Templates not updating
```bash
# Solution: Clear browser cache or restart Flask
```

### Issue: Permissions error
```bash
# Solution: Check file permissions
chmod 755 backend/
```

## Useful Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/14/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/)
- [Chart.js](https://www.chartjs.org/docs/latest/)

---

Happy Coding! 🚀
