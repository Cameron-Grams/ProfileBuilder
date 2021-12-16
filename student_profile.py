from assignment_performance import AssignmentDetails


class StudentProfile:
    def __init__(self, email):
        self.email = email
        self.classes = set()
        self.assignments = []

    def enroll_class(self, class_number):
        self.classes.add(class_number)

    def record_assignment(self, class_number, assignment_number, raw_attempts=None):
        # convert list of raw attempts to list of datetime objects
        # create assignment object for class and assignment number
        # update with the datetime attempts
        self.classes.add(class_number)
        assignment = AssignmentDetails(assignment_number)
        self.assignments.append(assignment)


