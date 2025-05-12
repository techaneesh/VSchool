from app import create_app, db
from app.models import Teacher, Student, Lesson

app = create_app()

with app.app_context():
    db.create_all()  # Ensure tables exist

    # Add teachers
    t1 = Teacher(name='Aneesh Mishra')
    t2 = Teacher(name='Software Engineer')

    # Add students
    s1 = Student(name='Alfred')
    s2 = Student(name='Stanley')

    # Add lessons
    l1 = Lesson(title='Math Basics')
    l2 = Lesson(title='History of India')

    db.session.add_all([t1, t2, s1, s2, l1, l2])
    db.session.commit()

    print("Seeded successfully!")
    print("Teachers:")
    for t in Teacher.query.all():
        print(f"{t.id}: {t.name}")
    print("Students:")
    for s in Student.query.all():
        print(f"{s.id}: {s.name}")
    print("Lessons:")
    for l in Lesson.query.all():
        print(f"{l.id}: {l.title}")
