class MyCM:
    def __init__(self, filename):
        self.name = filename

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()


from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


with open_file("my_file.txt") as f:
    f.write("Witamson z generatora")
