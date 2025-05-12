# VSchool Lesson Assignment API – VOPA Assignment

This project is a backend API for **V-School**, built with **Flask** and **SQLAlchemy**, allowing teachers to assign lessons to students, and students to mark them as complete.

---

## 🌐 Hosted API

**🔗 Live URL:** [https://aneesh.pythonanywhere.com](https://aneesh.pythonanywhere.com)

---

## ✅ Features Implemented

- Teachers can assign existing lessons to individual students.
- Students can view their assigned (incomplete) lessons.
- Students can mark assigned lessons as completed.
- Teachers can view completion statuses of their assigned lessons.

---

## 📦 Tech Stack

- **Backend Framework:** Flask
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Hosting:** PythonAnywhere
- **Tools:** Postman for API testing

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/techaneesh/VSchool.git
cd vschool_api

# Create a virtualenv
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py

# Use the seed.py script to create sample teachers, students, and lessons
python seed.py
