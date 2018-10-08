class FakeInput:

    def __init__(self, input1, input2):
       self.count = 0
       self.input1 = input1
       self.input2 = input2

    def increment_count(self):
        self.count += 1

    def get_input(self, message):
        self.increment_count()
        if self.count == 1: 
            return self.input1
        if self.count == 2:
            return self.input2

    def reset_count(self):
        self.count = 0
        