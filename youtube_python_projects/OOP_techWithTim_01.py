class Dog():

    def __init__(self, name, age, legs, tail):
        self.name = name
        self.age = age
        self.legs = legs
        self.tail = tail

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def speak_and_bark(self):
        print ("I am {}, hear me BARK!".format(self.name))

    def apendages(self):
        print ("{} has {} total appendages".format(self.name, self.legs + self.tail))

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age # 5 - 18
        self.grade = grade # 0 -100

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        raise IndexError ("Cannot add any more students to this course")

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


"""
CREATE DOGS HERE
"""
d1 = Dog("Dog One", 8, 4, 1)
d2 = Dog("Dog Two", 12, 0, 0)

"""
CREATE STUDENTS HERE
"""
s1 = Student("Evan", 25, 95)
s2 = Student("Karis", 19, 60)
s3 = Student("Christian", 99, 3)
s4 = Student("Caramon", 24, 85)
s5 = Student("Cason", 21, 87)

"""
TEST DOGS HERE
"""
print("---------------")
print(type(d1))
print(type(d2))
d1.speak_and_bark()
d2.speak_and_bark()
d1.apendages()
d2.apendages()
d1.set_age(33)
d2.set_age(1200)
print(d1.age)
print(d2.age)
print("---------------")

"""
TEST STUDENTS HERE
"""
course_Science = Course("Science", 4)
course_Science.add_student(s1)
course_Science.add_student(s2)
course_Science.add_student(s3)
course_Science.add_student(s4)
# course_Science.add_student(s5) this will raise an error


print("---------------")
print(course_Science.students[0].name)
print(course_Science.students[1].name)
print(course_Science.students[2].name)
print(course_Science.get_average_grade())