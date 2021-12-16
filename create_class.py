import os
import pickle
from student_profile import StudentProfile

def create_class(source_dir, class_number, assignment_number):
    all_students = []
    students = os.listdir(source_dir)
    print("Student directories found: ", students)

    with open("./PROFILES/STUDENT_PROFILES.pkl", "wb") as file:
        for student in students:
            new_student = StudentProfile(student)
            new_student.record_assignment(class_number, assignment_number)
            print("in create class with new student: ", new_student.assignments)
            all_students.append(new_student)
        output = pickle.dumps(all_students)
        file.write(output)
