
class Filereader(): 
    def __init__(self):
        pass

    def read_all(self, f):
        x = f.read()
        return x

    def rewind(self, f, n):
        y = f.seek(n)
        return y

    def get_line(self, f):
        z = f.readline()
        return z

