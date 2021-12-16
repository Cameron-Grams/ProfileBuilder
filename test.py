import pickle
import os
import sys
# This is the idiom to make the parent directory accessible for import
[sys.path.append(i) for i in ['.', '..']]

from student_profile import StudentProfile

with open('STUDENT_PROFILES.pkl', 'rb') as file:
    af = pickle.load(file)
    for a in af:
        print(a.email)
        print(a.assignments[0].num_attempts)
        print(a.assignments[0].attempts)

file.close()
