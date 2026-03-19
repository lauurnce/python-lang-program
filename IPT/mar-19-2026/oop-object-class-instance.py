class Dog:
    # Class attribute
    species = "Canis familiaris"
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
 
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4)

# 1. Accessing attributes
print(miles.name)      # Output: Miles
print(miles.species)   # Output: Canis familiaris

# 2. Calling the instance methods
print(miles.description())      # Output: Miles is 4 years old
print(miles.speak("Woof Woof"))  # Output: Miles says Woof Woof