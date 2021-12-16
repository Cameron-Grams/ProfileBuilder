import os
import pickle
from student_profile import StudentProfile

def create_class(source_dir, class_number, assignment_number):
    all_students = []
    students = os.listdir(source_dir)
    # DEBUG print("Student directories found: ", students)

    with open("./PROFILES/STUDENT_PROFILES.pkl", "wb") as file:
        for student in students:
            student_attempts = os.listdir(f"{source_dir}/{student}")
            # DEBUG print(f"{student} with attempts: ", student_attempts)

            new_student = StudentProfile(student)
            print("in create class with new student: ", new_student.email)
            new_student.record_assignment(class_number, assignment_number, student_attempts)
            print("in create class with new student: ", new_student.assignments)


            all_students.append(new_student)
        output = pickle.dumps(all_students)
        file.write(output)
