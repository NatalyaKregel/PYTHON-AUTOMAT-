class NegativeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class LargeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FloatNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


