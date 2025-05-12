from flask import Blueprint, request, jsonify
from app import db
from app.models import Assignment
from datetime import datetime
from app.models import Teacher, Student, Lesson

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route('/api/assignments', methods=['POST'])
def assign_lesson():
    data = request.json
    required_fields = ['teacher_id', 'student_id', 'lesson_id', 'due_date']
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    
    teacher = Teacher.query.get(data['teacher_id'])
    if not teacher:
        return jsonify({"error": "Invalid teacher_id"}), 404

    student = Student.query.get(data['student_id'])
    if not student:
        return jsonify({"error": "Invalid student_id"}), 404

    lesson = Lesson.query.get(data['lesson_id'])
    if not lesson:
        return jsonify({"error": "Invalid lesson_id"}), 404

    try:
        due_date = datetime.fromisoformat(data['due_date'])
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    assignment = Assignment(
        teacher_id=data['teacher_id'],
        student_id=data['student_id'],
        lesson_id=data['lesson_id'],
        due_date=datetime.fromisoformat(data['due_date'])
    )
    db.session.add(assignment)
    db.session.commit()
    return jsonify({
        "assignment_id": assignment.id,
        "teacher_id": assignment.teacher_id,
        "student_id": assignment.student_id,
        "lesson_id": assignment.lesson_id,
        "status": assignment.status,
        "assigned_at": assignment.assigned_at.isoformat(),
        "due_date": assignment.due_date.isoformat()
    }), 201

@assignment_bp.route('/api/students/<int:student_id>/assignments')
def get_assignments(student_id):
    status = request.args.get('status')
    query = Assignment.query.filter_by(student_id=student_id)

    if status:
        query = query.filter_by(status=status)
    return jsonify([
        {
            "assignment_id": a.id,
            "lesson_id": a.lesson_id,
            "status": a.status,
            "due_date": a.due_date.isoformat() if a.due_date else None
        } for a in query.all()
    ])

@assignment_bp.route('/api/assignments/<int:assignment_id>/complete', methods=['PATCH'])
def complete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if assignment.status == 'completed':
        return jsonify({"message": "Already completed"})
    assignment.status = 'completed'
    assignment.completed_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "Assignment marked as complete."})

@assignment_bp.route('/api/teachers/<int:teacher_id>/assignments/status')
def teacher_assignments(teacher_id):
    assignments = Assignment.query.filter_by(teacher_id=teacher_id).all()
    return jsonify([
        {
            "assignment_id": a.id,
            "student_id": a.student_id,
            "lesson_id": a.lesson_id,
            "status": a.status,
            "assigned_at": a.assigned_at.isoformat(),
            "completed_at": a.completed_at.isoformat() if a.completed_at else None
        } for a in assignments
    ])
