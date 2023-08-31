
class StudentException(Exception):
    pass

class StudentNameError(StudentException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidSubjectError(StudentException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidGradeError(StudentException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidTestError(StudentException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

