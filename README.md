# MentorMind - Mentorship Management System

A comprehensive web-based platform that digitally connects students, mentors, and administrators to manage the complete mentorship lifecycle.

## 🎯 Features

### 👤 Student Features
- **User Authentication** - Secure registration and login
- **Mentor Assignment** - View assigned mentor and expertise
- **Session Booking** - Request and schedule mentoring sessions
- **Progress Tracking** - Monitor skill development and task completion
- **Feedback System** - Rate and review mentoring sessions
- **Career Roadmap** - Personalized growth path and milestones
- **Notifications** - Real-time updates on sessions and tasks

### 🤝 Mentor Features
- **Student Management** - View and manage assigned mentees
- **Session Scheduling** - Create and manage mentoring sessions
- **Task Assignment** - Assign tasks and track progress
- **Performance Analytics** - View student feedback and ratings
- **Progress Monitoring** - Track mentee skill development

### 👨‍💼 Admin Features
- **User Management** - Add, edit, and manage users
- **Mentor Allocation** - Assign mentors to students
- **Announcements** - Post system-wide announcements
- **Analytics Dashboard** - View system statistics and reports
- **Session Monitoring** - Track all mentoring sessions

## 🛠 Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MySQL/SQLite
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login
- **Security**: Werkzeug

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5** - Responsive UI framework
- **JavaScript** - Client-side interactions
- **Chart.js** - Data visualization

## 📁 Project Structure

```
MentorMind/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   └── models.py          # Database models
│   │   ├── routes/
│   │   │   ├── auth.py            # Authentication routes
│   │   │   ├── student.py         # Student routes
│   │   │   ├── mentor.py          # Mentor routes
│   │   │   └── admin.py           # Admin routes
│   │   ├── templates/
│   │   │   ├── base.html          # Base template
│   │   │   ├── auth/              # Auth templates
│   │   │   ├── student/           # Student templates
│   │   │   ├── mentor/            # Mentor templates
│   │   │   └── admin/             # Admin templates
│   │   └── __init__.py            # Flask app initialization
│   └── requirements.txt           # Python dependencies
├── frontend/
│   ├── pages/                     # HTML pages
│   └── static/
│       ├── css/
│       │   └── style.css          # Custom styles
│       └── js/
│           └── main.js            # JavaScript utilities
├── database/
│   └── schema.sql                 # Database schema
├── config/
│   └── config.py                  # Configuration settings
├── run.py                         # Application entry point
└── .env                           # Environment variables
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL 8.0+ (or SQLite for development)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
cd e:\MentorMind
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4: Configure Database
Edit `.env` file and update database credentials:
```
DATABASE_URL=mysql+pymysql://username:password@localhost/mentormind
```

### Step 5: Initialize Database
```bash
# Create database
mysql -u root -p
CREATE DATABASE mentormind;

# Run schema
mysql -u root -p mentormind < database/schema.sql
```

### Step 6: Run Application
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 📊 Database Schema

### Key Tables
- **users** - User account information
- **student_profiles** - Student-specific data
- **mentor_profiles** - Mentor expertise and availability
- **mentor_mapping** - Student-mentor relationships
- **sessions** - Mentoring sessions
- **tasks** - Goals and assignments
- **feedback** - Session ratings and reviews
- **announcements** - System announcements
- **notifications** - User notifications

## 🔐 Authentication

- Passwords are hashed using Werkzeug security
- Session-based authentication with Flask-Login
- Role-based access control (RBAC)
- Protected routes for authenticated users only

## 🎨 UI/UX Features

- Clean, academic-themed interface
- Responsive design for all devices
- Bootstrap components for consistency
- Interactive dashboards with Charts.js
- Real-time notifications
- Smooth animations and transitions

## 📝 API Routes

### Authentication
- `GET /` - Landing page
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### Student Routes
- `GET /student/dashboard` - Student dashboard
- `GET /student/sessions` - View/schedule sessions
- `GET /student/progress` - Progress tracking
- `GET /student/career-roadmap` - Career roadmap
- `POST /student/feedback/<id>` - Submit feedback

### Mentor Routes
- `GET /mentor/dashboard` - Mentor dashboard
- `GET /mentor/students` - View mentees
- `GET /mentor/student/<id>` - View student details
- `POST /mentor/assign-task/<id>` - Assign task
- `GET /mentor/sessions` - View sessions

### Admin Routes
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/users` - Manage users
- `POST /admin/mentor-allocation` - Allocate mentors
- `POST /admin/announcements` - Create announcements
- `GET /admin/analytics` - View analytics

## 🔄 Workflow

### Student Journey
1. Register as Student
2. Complete profile information
3. Admin allocates mentor
4. Schedule mentoring sessions
5. Receive task assignments
6. Track progress and skills
7. Rate and provide feedback
8. Follow career roadmap

### Mentor Journey
1. Register as Mentor
2. Complete profile with expertise
3. View assigned students
4. Schedule and conduct sessions
5. Assign tasks and goals
6. Track student progress
7. Monitor feedback scores
8. Provide guidance and support

### Admin Journey
1. Manage user accounts
2. Allocate mentors to students
3. Monitor all sessions
4. Post announcements
5. View analytics and reports
6. Manage system settings

## 📈 Analytics Features

- Session completion statistics
- Mentor rating distribution
- Task completion rates
- Student progress metrics
- System usage analytics
- Performance reports

## 🔧 Configuration

Edit `config/config.py` to customize:
- Database connection
- Session timeout
- Security settings
- Email notifications (future)
- API rate limiting (future)

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
- Check MySQL is running
- Verify credentials in .env
- Ensure database exists

**Module Import Error**
- Activate virtual environment
- Run `pip install -r requirements.txt`
- Check Python path

**Port Already in Use**
- Change port in `run.py`
- Kill process on port 5000

## 📚 Dependencies

See `backend/requirements.txt` for complete list:
- Flask 2.3.2
- Flask-SQLAlchemy 3.0.5
- Flask-Login 0.6.2
- PyMySQL 1.1.0
- python-dotenv 1.0.0

## 🚀 Future Enhancements

- Email notifications
- Video conferencing integration
- AI-powered mentor matching
- Mobile app
- Advanced reporting
- Certification management
- Peer feedback system

## 📄 License

This project is created for educational purposes.

## 👥 Contributors

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Flask, Python
- **Database**: MySQL, SQLAlchemy

## 📧 Support

For issues or questions, please create an issue or contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: February 11, 2026
