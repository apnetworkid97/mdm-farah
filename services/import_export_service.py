import json
import csv

from models.student import Student
from services.storage_service import get_data_file


def load_students():
    students_file = get_data_file("students.json")

    if not students_file.exists():

        return []

    with open(students_file, "r", encoding="utf-8") as file:

        data = json.load(file)

    return [Student.from_dict(item) for item in data]


def save_students(students):
    students_file = get_data_file("students.json")

    with open(students_file, "w", encoding="utf-8") as file:

        json.dump([student.to_dict() for student in students], file, indent=4)


def export_json(output_file):

    students = load_students()

    with open(output_file, "w", encoding="utf-8") as file:

        json.dump([student.to_dict() for student in students], file, indent=4)


def import_json(input_file):

    with open(input_file, "r", encoding="utf-8") as file:

        data = json.load(file)

    students = [Student.from_dict(item) for item in data]

    save_students(students)


def export_csv(output_file):

    students = load_students()

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["nim", "full_name", "major", "year", "gpa", "email", "phone"],
        )

        writer.writeheader()

        for student in students:

            writer.writerow(student.to_dict())


def import_csv(input_file):

    students = []

    with open(input_file, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            students.append(Student.from_dict(row))

    save_students(students)
