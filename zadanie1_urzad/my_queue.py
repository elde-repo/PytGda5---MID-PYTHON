class MyQueue:
    def __init__(self):
        self.begin = 0
        self.end = 0

    def add_element(self):
        self.end += 1
        return self.end

    def remove_element(self):
        if self.begin < self.end:
            self.begin += 1
            return self.begin
        return None
