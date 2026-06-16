class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def student_details(self):
        return (f'Name:{self.name} \nAge: {self.age}') 
s1 = Student("mehedi",20)
print(s1.student_details())