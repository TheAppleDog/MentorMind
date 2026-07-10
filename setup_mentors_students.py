"""
Setup script to populate database with 5 mentors and 10 students with complete data
"""

import sys
import os
from datetime import datetime, timedelta, time
import random

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from app.models.models import (
    db, User, MentorProfile, StudentProfile, MentorMapping, Session, Task,
    SkillTracking, Feedback, Milestone, CareerRoadmap, SessionNotes, MentorQuality
)

app = create_app()

# Mentor data
MENTORS = [
    {
        'name': 'Ritvi Shah',
        'email': 'ritvi.shah@mentormind.com',
        'password': 'Ritvi@123456',
        'expertise': 'Full Stack Development, Web Technologies, JavaScript, React.js',
        'experience_years': 8,
        'specialization': 'Web Development',
        'bio': 'Senior Full Stack Developer with 8 years of experience in building scalable web applications.',
        'professional_title': 'Senior Full Stack Developer',
        'organization': 'Tech Solutions Inc.',
        'certifications': 'AWS Solutions Architect, JavaScript Expert, React Certified',
        'max_mentees': 8,
        'hourly_rate': 50.0
    },
    {
        'name': 'Nikhil Kashyap',
        'email': 'nikhil.kashyap@mentormind.com',
        'password': 'Nikhil@123456',
        'expertise': 'Data Science, Machine Learning, Python, Data Analysis',
        'experience_years': 6,
        'specialization': 'Data Science & ML',
        'bio': 'Data Science expert with strong background in machine learning and predictive analytics.',
        'professional_title': 'Senior Data Scientist',
        'organization': 'Data Insights Corp',
        'certifications': 'Machine Learning Specialist, Python Expert, TensorFlow Certified',
        'max_mentees': 6,
        'hourly_rate': 55.0
    },
    {
        'name': 'Riya Arora',
        'email': 'riya.arora@mentormind.com',
        'password': 'Riya@123456',
        'expertise': 'Cloud Architecture, AWS, DevOps, Infrastructure',
        'experience_years': 7,
        'specialization': 'Cloud & DevOps',
        'bio': 'Cloud architect specializing in AWS infrastructure and DevOps practices.',
        'professional_title': 'Cloud Solutions Architect',
        'organization': 'CloudTech Systems',
        'certifications': 'AWS Solutions Architect Professional, Kubernetes Expert, Docker Certified',
        'max_mentees': 7,
        'hourly_rate': 60.0
    },
    {
        'name': 'Naina Mathur',
        'email': 'naina.mathur@mentormind.com',
        'password': 'Naina@123456',
        'expertise': 'Mobile Development, Flutter, iOS, Android',
        'experience_years': 5,
        'specialization': 'Mobile App Development',
        'bio': 'Mobile developer with expertise in cross-platform development using Flutter.',
        'professional_title': 'Senior Mobile Developer',
        'organization': 'MobileFirst Apps',
        'certifications': 'Flutter Expert, iOS Development Certified, Mobile Architecture Specialist',
        'max_mentees': 5,
        'hourly_rate': 45.0
    },
    {
        'name': 'Nimit Jha',
        'email': 'nimit.jha@mentormind.com',
        'password': 'Nimit@123456',
        'expertise': 'Database Design, SQL, NoSQL, System Design',
        'experience_years': 9,
        'specialization': 'Backend & Databases',
        'bio': 'Senior backend engineer with expertise in database design and system architecture.',
        'professional_title': 'Senior Backend Engineer',
        'organization': 'Enterprise Systems Ltd',
        'certifications': 'Database Design Expert, System Architecture Certified, SQL Specialist',
        'max_mentees': 8,
        'hourly_rate': 58.0
    }
]

# Student data
STUDENTS = [
    {
        'name': 'Arjun Kumar',
        'email': 'arjun.kumar@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Third Year',
        'major': 'Computer Science',
        'gpa': 3.8,
        'interests': 'Web Development, Open Source',
        'skills': 'Python, JavaScript, HTML/CSS, React',
        'career_goals': 'Become a Full Stack Developer'
    },
    {
        'name': 'Priya Sharma',
        'email': 'priya.sharma@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Second Year',
        'major': 'Data Science',
        'gpa': 3.9,
        'interests': 'Machine Learning, Data Analytics',
        'skills': 'Python, SQL, Pandas, Numpy, Scikit-learn',
        'career_goals': 'Data Scientist at Top Tech Company'
    },
    {
        'name': 'Aditya Patel',
        'email': 'aditya.patel@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Third Year',
        'major': 'Computer Science',
        'gpa': 3.7,
        'interests': 'Cloud Computing, DevOps',
        'skills': 'Linux, AWS, Docker, Kubernetes',
        'career_goals': 'Cloud Solutions Architect'
    },
    {
        'name': 'Divya Singh',
        'email': 'divya.singh@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Second Year',
        'major': 'Computer Science',
        'gpa': 3.6,
        'interests': 'Mobile Development, UI/UX',
        'skills': 'Flutter, Dart, Swift, Java',
        'career_goals': 'iOS App Developer'
    },
    {
        'name': 'Rahul Verma',
        'email': 'rahul.verma@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'First Year',
        'major': 'Computer Science',
        'gpa': 3.5,
        'interests': 'Web Development, Databases',
        'skills': 'Java, SQL, Basic Web Dev',
        'career_goals': 'Backend Engineer'
    },
    {
        'name': 'Neha Gupta',
        'email': 'neha.gupta@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Third Year',
        'major': 'IT',
        'gpa': 3.8,
        'interests': 'Full Stack, Web Technologies',
        'skills': 'JavaScript, Node.js, React, MongoDB',
        'career_goals': 'MERN Stack Developer'
    },
    {
        'name': 'Vipul Desai',
        'email': 'vipul.desai@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Second Year',
        'major': 'Computer Science',
        'gpa': 3.4,
        'interests': 'Data Science, AI',
        'skills': 'Python, TensorFlow, Keras',
        'career_goals': 'Machine Learning Engineer'
    },
    {
        'name': 'Isha Kapoor',
        'email': 'isha.kapoor@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'First Year',
        'major': 'Computer Science',
        'gpa': 3.9,
        'interests': 'Software Engineering, System Design',
        'skills': 'C++, Python, System Design',
        'career_goals': 'Software Engineer at FAANG'
    },
    {
        'name': 'Karan Chopra',
        'email': 'karan.chopra@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Third Year',
        'major': 'Information Technology',
        'gpa': 3.7,
        'interests': 'Cybersecurity, Network Security',
        'skills': 'Networking, Linux, Security Tools',
        'career_goals': 'Cybersecurity Analyst'
    },
    {
        'name': 'Anjali Nair',
        'email': 'anjali.nair@student.mentormind.com',
        'password': 'Student@123456',
        'academic_level': 'Second Year',
        'major': 'Computer Science',
        'gpa': 3.6,
        'interests': 'Web Development, Frontend',
        'skills': 'HTML, CSS, JavaScript, Vue.js',
        'career_goals': 'Frontend Developer'
    }
]

# Mentor-Student mapping (2 students per mentor)
MENTOR_STUDENT_MAPPING = [
    (0, [0, 5]),  # Ritvi -> Arjun, Neha
    (1, [1, 6]),  # Nikhil -> Priya, Vipul
    (2, [2, 9]),  # Riya -> Aditya, Karan
    (3, [3, 7]),  # Naina -> Divya, Isha
    (4, [4, 8])   # Nimit -> Rahul, Isha
]

def create_mentors():
    """Create mentor users with profiles"""
    print("\n📚 Creating 5 Mentors...")
    mentors = []
    
    for mentor_data in MENTORS:
        # Check if mentor already exists
        existing = User.query.filter_by(email=mentor_data['email']).first()
        if existing:
            print(f"  ✓ {mentor_data['name']} already exists")
            mentors.append(existing)
            continue
        
        # Create user
        user = User(
            name=mentor_data['name'],
            email=mentor_data['email'],
            role='mentor'
        )
        user.set_password(mentor_data['password'])
        db.session.add(user)
        db.session.flush()
        
        # Create mentor profile
        mentor_profile = MentorProfile(
            mentor_id=user.user_id,
            expertise=mentor_data['expertise'],
            experience_years=mentor_data['experience_years'],
            specialization=mentor_data['specialization'],
            bio=mentor_data['bio'],
            professional_title=mentor_data['professional_title'],
            organization=mentor_data['organization'],
            certifications=mentor_data['certifications'],
            max_mentees=mentor_data['max_mentees'],
            hourly_rate=mentor_data['hourly_rate'],
            is_approved=True,
            approval_date=datetime.utcnow(),
            average_rating=4.8,
            total_sessions=0
        )
        db.session.add(mentor_profile)
        
        # Create mentor quality record
        mentor_quality = MentorQuality(
            mentor_id=user.user_id,
            overall_rating=4.8,
            session_count=0,
            completion_rate=100.0,
            student_satisfaction=4.8,
            response_time_hours=2.0,
            last_active=datetime.utcnow(),
            is_active=True,
            is_top_mentor=True
        )
        db.session.add(mentor_quality)
        
        db.session.commit()
        mentors.append(user)
        print(f"  ✓ Created {mentor_data['name']} ({mentor_data['email']})")
    
    return mentors

def create_students():
    """Create student users with profiles"""
    print("\n👨‍🎓 Creating 10 Students...")
    students = []
    
    for student_data in STUDENTS:
        # Check if student already exists
        existing = User.query.filter_by(email=student_data['email']).first()
        if existing:
            print(f"  ✓ {student_data['name']} already exists")
            students.append(existing)
            continue
        
        # Create user
        user = User(
            name=student_data['name'],
            email=student_data['email'],
            role='student'
        )
        user.set_password(student_data['password'])
        db.session.add(user)
        db.session.flush()
        
        # Create student profile
        student_profile = StudentProfile(
            student_id=user.user_id,
            academic_level=student_data['academic_level'],
            major=student_data['major'],
            gpa=student_data['gpa'],
            interests=student_data['interests'],
            skills=student_data['skills'],
            career_goals=student_data['career_goals']
        )
        db.session.add(student_profile)
        db.session.commit()
        students.append(user)
        print(f"  ✓ Created {student_data['name']} ({student_data['email']})")
    
    return students

def assign_mentors(mentors, students):
    """Assign mentors to students"""
    print("\n🔗 Assigning Mentors to Students...")
    
    for mentor_idx, student_indices in MENTOR_STUDENT_MAPPING:
        mentor = mentors[mentor_idx]
        for student_idx in student_indices:
            student = students[student_idx]
            
            # Check if mapping already exists
            existing = MentorMapping.query.filter_by(
                student_id=student.user_id,
                mentor_id=mentor.user_id
            ).first()
            
            if existing:
                print(f"  ✓ {student.name} already assigned to {mentor.name}")
                continue
            
            mapping = MentorMapping(
                student_id=student.user_id,
                mentor_id=mentor.user_id,
                status='active'
            )
            db.session.add(mapping)
        
        db.session.commit()
        print(f"  ✓ {mentor.name} assigned to 2 students")

def create_sessions(mentors, students):
    """Create sessions for student-mentor pairs"""
    print("\n📅 Creating Sessions...")
    
    session_topics = [
        'Introduction and Goal Setting',
        'Career Planning Discussion',
        'Technical Skills Assessment',
        'Project Review',
        'Resume Review',
        'Interview Preparation',
        'Code Review Session',
        'Progress Check-in'
    ]
    
    for mentor_idx, student_indices in MENTOR_STUDENT_MAPPING:
        mentor = mentors[mentor_idx]
        for student_idx in student_indices:
            student = students[student_idx]
            
            # Create 3-4 sessions for each student
            num_sessions = random.randint(3, 4)
            for i in range(num_sessions):
                session_date = datetime.utcnow() + timedelta(days=random.randint(-30, 30))
                session_hour = random.randint(10, 17)
                session_time = time(hour=session_hour, minute=0, second=0)
                
                session = Session(
                    student_id=student.user_id,
                    mentor_id=mentor.user_id,
                    session_date=session_date.date(),
                    session_time=session_time,
                    duration_minutes=60,
                    topic=random.choice(session_topics),
                    description=f"Session between {student.name} and {mentor.name}",
                    status=random.choice(['completed', 'scheduled', 'approved']),
                    approval_status='approved',
                    completed_at=session_date if random.random() > 0.5 else None
                )
                db.session.add(session)
            
            db.session.commit()
            print(f"  ✓ Created {num_sessions} sessions for {student.name}")

def create_tasks(students):
    """Create tasks for students"""
    print("\n✅ Creating Tasks...")
    
    task_titles = [
        'Complete JavaScript Fundamentals Course',
        'Build Portfolio Project',
        'Learn Database Design',
        'Practice Data Structures',
        'Build REST API',
        'Master Git and GitHub',
        'Complete Coding Challenge',
        'Interview Preparation'
    ]
    
    for student in students:
        # Create 4-6 tasks per student
        num_tasks = random.randint(4, 6)
        for i in range(num_tasks):
            task = Task(
                student_id=student.user_id,
                title=random.choice(task_titles),
                description=f"Important task for {student.name}",
                deadline=datetime.utcnow() + timedelta(days=random.randint(7, 60)),
                status=random.choice(['pending', 'in-progress', 'completed']),
                priority=random.choice(['low', 'medium', 'high']),
                progress_percentage=random.randint(0, 100)
            )
            db.session.add(task)
        
        db.session.commit()
        print(f"  ✓ Created {num_tasks} tasks for {student.name}")

def create_skills(students):
    """Create skill tracking for students"""
    print("\n🎯 Creating Skill Tracking...")
    
    skills = [
        'Python', 'JavaScript', 'Java', 'C++', 'SQL',
        'React', 'Node.js', 'Flask', 'Django',
        'Machine Learning', 'Data Analysis', 'System Design',
        'Problem Solving', 'Communication'
    ]
    
    for student in students:
        # Assign 8-10 skills per student
        student_skills = random.sample(skills, k=random.randint(8, 10))
        
        for skill in student_skills:
            skill_track = SkillTracking(
                student_id=student.user_id,
                skill_name=skill,
                level=random.choice(['beginner', 'intermediate', 'advanced']),
                proficiency_score=random.randint(30, 95)
            )
            db.session.add(skill_track)
        
        db.session.commit()
        print(f"  ✓ Created skills for {student.name}")

def create_feedback(mentors, students):
    """Create feedback records"""
    print("\n⭐ Creating Feedback...")
    
    feedback_comments = [
        'Great progress! Keep it up.',
        'Excellent understanding of concepts.',
        'Need to focus more on hands-on projects.',
        'Very consistent and dedicated.',
        'Good technical knowledge, work on soft skills.',
        'Impressive problem-solving ability.',
        'Shows great potential for growth.',
        'Participate more in discussions.',
        'Well-structured approach to problems.',
        'Continue building real-world projects.'
    ]
    
    count = 0
    for mentor_idx, student_indices in MENTOR_STUDENT_MAPPING:
        mentor = mentors[mentor_idx]
        for student_idx in student_indices:
            student = students[student_idx]
            
            # Get completed sessions
            sessions = Session.query.filter_by(
                student_id=student.user_id,
                mentor_id=mentor.user_id,
                status='completed'
            ).all()
            
            for session in sessions[:2]:  # Create feedback for first 2 completed sessions
                feedback = Feedback(
                    session_id=session.session_id,
                    student_id=student.user_id,
                    mentor_id=mentor.user_id,
                    rating=random.randint(4, 5),
                    comment=random.choice(feedback_comments),
                    suggestion='Continue with current progress and explore advanced topics.'
                )
                db.session.add(feedback)
                count += 1
        
        db.session.commit()
    
    print(f"  ✓ Created {count} feedback records")

def create_career_roadmaps(mentors, students):
    """Create career roadmaps for students"""
    print("\n🗺️  Creating Career Roadmaps...")
    
    roadmap_stages = [
        ('Learning Basics', 'Build Fundamentals', 'Python, Data Structures, Web Dev'),
        ('Building Projects', 'Create Portfolio', 'Full Stack, Cloud, Databases'),
        ('Interview Prep', 'Get Internship', 'DSA, System Design, Behavioral'),
        ('Working on Internship', 'Land FTE', 'Advanced Topics, Leadership')
    ]
    
    placements = ['Pre-Placement', '2nd Sem', '3rd Sem', 'Placement Ready']
    
    for mentor_idx, student_indices in MENTOR_STUDENT_MAPPING:
        mentor = mentors[mentor_idx]
        for student_idx in student_indices:
            student = students[student_idx]
            
            # Check if roadmap exists
            existing = CareerRoadmap.query.filter_by(student_id=student.user_id).first()
            if existing:
                print(f"  ✓ {student.name} already has roadmap")
                continue
            
            stage_idx = random.randint(0, 2)
            current, next_stage, certs = roadmap_stages[stage_idx]
            
            roadmap = CareerRoadmap(
                student_id=student.user_id,
                mentor_id=mentor.user_id,
                current_stage=current,
                next_stage=next_stage,
                suggested_certifications=certs,
                internship_readiness=random.choice(['Not Ready', 'In Progress', 'Ready']),
                placement_stage=placements[stage_idx]
            )
            db.session.add(roadmap)
        
        db.session.commit()
        print(f"  ✓ Created roadmaps for {mentor.name}'s students")

def create_milestones(students):
    """Create milestones for students"""
    print("\n🏆 Creating Milestones...")
    
    milestone_titles = [
        'Complete First Project',
        'Master Core Concepts',
        'Get Interview Call',
        'Secure Internship',
        'Build Portfolio Website',
        'Achieve Target GPA',
        'Learn New Technology',
        'Pass Technical Assessment'
    ]
    
    for student in students:
        # Create 3-4 milestones per student
        num_milestones = random.randint(3, 4)
        for i in range(num_milestones):
            achieved = random.choice([True, False])
            milestone = Milestone(
                student_id=student.user_id,
                title=random.choice(milestone_titles),
                description=f"Milestone for {student.name}",
                target_date=datetime.utcnow() + timedelta(days=random.randint(30, 180)),
                achieved_date=datetime.utcnow() if achieved else None,
                status='achieved' if achieved else 'pending'
            )
            db.session.add(milestone)
        
        db.session.commit()
        print(f"  ✓ Created {num_milestones} milestones for {student.name}")

def print_credentials():
    """Print all login credentials"""
    print("\n" + "="*80)
    print("🔐 LOGIN CREDENTIALS")
    print("="*80)
    
    print("\n📚 MENTORS:")
    print("-" * 80)
    print(f"{'Name':<20} {'Email':<40} {'Password':<20}")
    print("-" * 80)
    for mentor in MENTORS:
        print(f"{mentor['name']:<20} {mentor['email']:<40} {mentor['password']:<20}")
    
    print("\n👨‍🎓 STUDENTS:")
    print("-" * 80)
    print(f"{'Name':<20} {'Email':<40} {'Password':<20}")
    print("-" * 80)
    for student in STUDENTS:
        print(f"{student['name']:<20} {student['email']:<40} {student['password']:<20}")
    
    print("\n" + "="*80)

def main():
    """Main setup function"""
    print("\n" + "="*80)
    print("🚀 MENTORMIND - MENTOR & STUDENT SETUP")
    print("="*80)
    
    with app.app_context():
        try:
            # Create tables if not exists
            db.create_all()
            
            # Create mentors
            mentors = create_mentors()
            
            # Create students
            students = create_students()
            
            # Assign mentors to students
            assign_mentors(mentors, students)
            
            # Create sessions
            create_sessions(mentors, students)
            
            # Create tasks
            create_tasks(students)
            
            # Create skills
            create_skills(students)
            
            # Create feedback
            create_feedback(mentors, students)
            
            # Create career roadmaps
            create_career_roadmaps(mentors, students)
            
            # Create milestones
            create_milestones(students)
            
            # Print credentials
            print_credentials()
            
            print("\n✅ Setup completed successfully!")
            print(f"   Total Mentors: 5")
            print(f"   Total Students: 10")
            print(f"   Sessions Created: ~35")
            print(f"   Tasks Created: ~50")
            print(f"   Skills Tracked: ~100")
            
        except Exception as e:
            print(f"\n❌ Error during setup: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
