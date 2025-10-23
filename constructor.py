#Constructor
class Studnet:
    def __init__(self, name):
        self.name = name 

    def display(self):
        print('Hello, my name is', self.name)

student1 = Studnet('Cherry')

student1.display()
