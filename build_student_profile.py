import os
import argparse
from create_dir import create_dir
from create_class import create_class

"""
if there is a student_profiles pickle file in the student_profiles folder
open it and record -- This is a decision, should this program manage existing records
or should each assignment produce single collections?

if not create
"""

def main(source_dir, class_number, assignment_number):
    current_files = os.listdir()

    if 'PROFILES' in current_files:
        print("PROFILES found")
    else:
        create_dir('PROFILES')

    PROFILES_FILES = os.listdir('./PROFILES')
    if 'STUDENT_PROFILES.pkl' in PROFILES_FILES:
#        update_class(source_dir, class_number, assignment_number) <-- Next
        print("STUDENT_PROFILES.pkl found")
    else:
        create_class(source_dir, class_number, assignment_number)
#        DEBUG print("Creating new STUDENT_PROFILES")
    print("Exiting build_student_profile.main")


### Define the arguments needed to build profiles 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Adds users from wolverine access course roster to slack."
    )
    
    parser.add_argument(
        "--source",
        dest="source",
        action="store",
        required=True,
        help="absolute path to directory with the student files",
    )

    parser.add_argument(
        "--assignment",
        dest="assignment",
        action="store",
        required=True,
        help="Assignment name or number",
    )

    parser.add_argument(
        "--class-number",
        dest="class_number",
        action="store",
        required=True,
        help="class number for the assignments",
    )

    args = parser.parse_args()

    main(args.source, args.assignment, args.class_number)




