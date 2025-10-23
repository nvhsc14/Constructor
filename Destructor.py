#Constructor
class Studnet:
    def __init__(self, name):
        self.name = name 

    def display(self):
        print('Hello, My name is', self.name)

    def __del__(self):
        print("Object destroyed")

student1 = Studnet('Cherry')
student2 = Studnet('Kotilu')

del student2

student1.display()
student2.display()
