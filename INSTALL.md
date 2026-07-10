# MentorMind Project - Installation Guide

## System Requirements

- **OS**: Windows 10/11, macOS, or Linux
- **Python**: 3.8 or higher
- **MySQL**: 8.0+ (or SQLite for development)
- **RAM**: 2GB minimum
- **Storage**: 500MB

## Step-by-Step Installation

### Step 1: Install Python

1. Download Python from https://www.python.org/downloads/
2. Run installer and **check "Add Python to PATH"**
3. Verify installation:
   ```bash
   python --version
   ```

### Step 2: Install MySQL (Optional - Use SQLite for testing)

1. Download from https://dev.mysql.com/downloads/mysql/
2. Follow installation wizard
3. Start MySQL service

### Step 3: Clone/Download Project

Navigate to project directory:
```bash
cd e:\MentorMind
```

### Step 4: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 6: Setup Database

**Option A: MySQL**
```bash
# Create database
mysql -u root -p
CREATE DATABASE mentormind;
EXIT;

# Import schema
mysql -u root -p mentormind < ..\database\schema.sql
```

**Option B: SQLite (Easier for testing)**
```bash
# Edit .env
SQLALCHEMY_DATABASE_URI=sqlite:///mentormind.db

# Database auto-creates on first run
```

### Step 7: Configure Environment

Create/Edit `.env` file:
```
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mentormind.db
DEBUG=True
```

### Step 8: Run Application

```bash
# From project root
python run.py
```

### Step 9: Access Application

Open browser: **http://localhost:5000**

## Testing the Installation

1. **Register as Student**
   - Click "Register"
   - Fill form with Student role
   - Login with credentials

2. **Register as Mentor**
   - Register another account with Mentor role

3. **Admin Setup**
   - Login to MySQL
   - Insert admin user:
     ```sql
     INSERT INTO users (name, email, password_hash, role) 
     VALUES ('Admin', 'admin@mentormind.com', 'hash', 'admin');
     ```

## Troubleshooting

### Python Not Found
- Ensure Python is in PATH
- Restart terminal after installing Python
- Use full path: `C:\Python39\python.exe`

### Database Connection Error
```
Error: Can't connect to MySQL server
```
- Ensure MySQL is running
- Check credentials in .env
- For SQLite, ensure write permissions

### Module Not Found
```
ModuleNotFoundError: No module named 'flask'
```
- Activate virtual environment
- Run `pip install -r requirements.txt` again
- Check no syntax errors in requirements.txt

### Port 5000 Already in Use
```bash
# Change port in run.py
app.run(port=5001)
```

## Project Structure Overview

```
e:\MentorMind\
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   └── models.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── student.py
│   │   │   ├── mentor.py
│   │   │   └── admin.py
│   │   └── templates/
│   │       ├── base.html
│   │       ├── auth/
│   │       ├── student/
│   │       ├── mentor/
│   │       └── admin/
│   └── requirements.txt
├── frontend/
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── database/
│   └── schema.sql
├── config/
│   └── config.py
├── run.py
├── .env
└── README.md
```

## First Time Setup Checklist

- [ ] Python installed and in PATH
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database created (MySQL or SQLite)
- [ ] `.env` file configured
- [ ] Application runs (`python run.py`)
- [ ] Can access `http://localhost:5000`
- [ ] Can register as student/mentor
- [ ] Can login successfully

## Next Steps

1. Read `README.md` for full feature overview
2. Check `QUICKSTART.md` for common tasks
3. Customize in `config/config.py`
4. Modify templates in `backend/app/templates/`
5. Add routes in `backend/app/routes/`

## Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Chart.js: https://www.chartjs.org/docs/latest/

## Support

If you encounter issues:
1. Check error message carefully
2. Search error on Google
3. Check `.env` and database configuration
4. Verify all dependencies installed
5. Ensure Python version compatibility

---

**Installation Complete!** 🎉  
You're ready to use MentorMind.
