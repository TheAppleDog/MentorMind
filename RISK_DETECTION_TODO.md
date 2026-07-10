# Automatic Risk Detection - Implementation TODO

## Task Overview
Implement automatic risk detection that monitors:
- Session attendance
- Task completion
- Feedback scores  
- Progress rate

Students with declining performance are flagged as "At Risk" and mentors/admins are alerted.

## Implementation Steps

### Step 1: Add Risk Detection Model
- [x] Add RiskAlert model to backend/app/models/models.py
- [x] Add fields: student_id, mentor_id, risk_level, session_attendance_rate, task_completion_rate, avg_feedback_score, progress_rate, risk_factors, recommendations, created_at, updated_at, resolved_at

### Step 2: Add Risk Detection Algorithm
- [x] Create risk calculation function in backend/app/routes/mentor.py
- [x] Calculate metrics: session attendance, task completion, feedback scores, progress rate
- [x] Determine risk level: Low (green), Medium (yellow), High (orange), Critical (red)

### Step 3: Add Risk Detection API Routes
- [x] Add route: /api/students/<int:student_id>/risk (GET - get student risk)
- [x] Add route: /api/students/risk/all (GET - get all at-risk students for mentor)
- [x] Add route: /api/students/risk/refresh (POST - recalculate all risks)
- [x] Add route: /api/students/<int:student_id>/risk/resolve (POST - resolve risk alert)

### Step 4: Update Mentor Dashboard
- [x] Add "At Risk" students section in mentor dashboard
- [x] Show risk badge on student cards with color coding
- [x] Display metrics: attendance, task completion, feedback, progress

### Step 5: Update Database Schema
- [x] Add risk_alerts table to database/schema.sql

## How Risk Detection Works

### Risk Calculation Algorithm
The system calculates risk based on four key metrics:
1. **Session Attendance Rate** (30% weight) - Percentage of completed sessions
2. **Task Completion Rate** (30% weight) - Percentage of completed tasks
3. **Feedback Score** (20% weight) - Average rating from mentors
4. **Progress Rate** (20% weight) - Based on skill proficiency scores

### Risk Levels
- **Low** (Score < 20): Student is performing well
- **Medium** (Score 20-40): Some concerns, monitor closely
- **High** (Score 40-60): Intervention needed
- **Critical** (Score >= 60): Urgent intervention required

### Risk Factors Detected
- low_attendance / declining_attendance
- missed_deadlines / delayed_tasks
- poor_feedback / average_feedback
- stalled_progress / slow_progress

### Notifications
When a student's risk level increases to "High" or "Critical", the system automatically:
1. Creates a RiskAlert record
2. Sends a notification to the mentor
3. Displays the student in the "At-Risk Students" section on the dashboard

## API Usage

### Get Student Risk
```bash
GET /mentor/api/students/<student_id>/risk
```

### Get All At-Risk Students
```bash
GET /mentor/api/students/risk/all
```

### Refresh All Risks
```bash
POST /mentor/api/students/risk/refresh
```

### Resolve Risk Alert
```bash
POST /mentor/api/students/<student_id>/risk/resolve
```

