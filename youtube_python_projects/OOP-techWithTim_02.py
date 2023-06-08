class Pet():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I'm {self.color}.")
    def speak(self):
        print("(PET CLASS) - def speak: 'default text'")

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def speak(self):
            print("Mau")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def speak(self):
            print("Roarf") 

"""
TEST CODE HERE
"""
p = Pet("Michaiah", 25, "Brown")
c = Cat("Pixel", 3, "Brown")
d = Dog("Dogmeat", 15, "Red")
p.show()
c.show()
d.show()
p.speak()
c.speak()
d.speak()
