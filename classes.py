class MyClass:
    x = 4


obj1 = MyClass()

print(obj1.x)


# ? init function

class Person:


    def __init__(self, name, age, natio):
        self.name = name
        self.age = age
        self.natio = natio

    def speak(self):
        print("i can speak")


person = Person("karim", 21, "ALG")

print(person.name, person.age, person.natio)

person.speak()


person.age = 22

print(person.name, person.age, person.natio)

del person.natio

print(Person)
print(person)


# child class

class Teacher(Person):
    def __init__(self, name, age, natio, job):
        super().__init__(name, age, natio)
    pass
 

class Student(Person):
    def __init__(self, name, age, natio, Id, study_feild, lvl):
        super().__init__(name, age, natio)
        self.Id = Id
        self.study_feild = study_feild
        self.lvl = lvl
        
    def add(self, a, b):
        return a + b


student = Student(name="stu_name", age=20, natio="ALG", Id=1, study_feild='st', lvl="L3")

print(student.name)

student.speak()


print(student.add(5, 5))

teacher = Teacher(name='test', age=15, natio="alg")

print(teacher.name)