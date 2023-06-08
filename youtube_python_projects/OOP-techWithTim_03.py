class Person:
    """Person class for defining people"""
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


"""
MAKE PEOPLE HERE
"""
p1 = Person("Evan")
p2 = Person("Michaiah")

"""
TEST DEFS HERE
"""
print(Person.number_of_people())
