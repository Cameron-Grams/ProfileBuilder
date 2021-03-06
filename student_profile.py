from datetime import datetime as dt
from datetime import timezone
from assignment_class import AssignmentDetails

class StudentProfile:
    def __init__(self, email):
        self.email = email
        self.classes = set()
        self.assignments = []

    def convert_attempts(self, raw_attempt):
        # string in milliseconds from the coursera time stamp
        seconds_value =  int(raw_attempt)/1000
        utc_time_obj = dt.fromtimestamp(seconds_value, tz=timezone.utc)
        return utc_time_obj

    def record_assignment(self, class_number, assignment_number, raw_attempts=None):
        # include new assignments in the student object
        assignment = AssignmentDetails(class_number, assignment_number)

        if raw_attempts:
            dtg_attempts = [self.convert_attempts(attempt) for attempt in raw_attempts]
            assignment.attempts = dtg_attempts
            assignment.num_attempts = len(dtg_attempts)

        self.classes.add(class_number)
        self.assignments.append(assignment)

        

