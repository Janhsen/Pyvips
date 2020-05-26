class Student:
    def __init__(self, name :str, age :int, grade:int):
        self.age = age
        self.name = name
        self.grade = grade  # 0 - 100

    def get_grade(self) -> int:
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students  = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student ('Tim', 29, 95)
s2 = Student ('Bill', 29, 75)
s3 = Student ('Jill', 29, 65)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())
print(course.students[0].name)


class Pet:
    def __init__(self, name :str , age: int):
        self.name = name    
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont speak")

class Cat(Pet):  
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 10)
p = p.speak()

c = Cat("Bill", 34, "Brown")
c = c.speak()

d = Dog("Bill do", 344)
d = d.speak()

 

class Person:
    number_of_people = 0
    Gravity = - 9.8

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def __init__(self, name):
        self.name = name
        self.add_person()

p1 = Person ("Tim")
p2 = Person ("Jill")

#Statische Methoden
class Math:

    @staticmethod
    def add5(x):
        return x +5 

print(Math.add5(4))