class Person:
    def __init__(self,name):
        self.person_name = name
        
    def introduce(self):
        print(f'Hello, my name is {self.person_name} ')

person_1 = Person("Mehedi")
person_add=person_1.introduce()

