# Simple Polymorphism Example in Python

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Demonstrating polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")

# Output:
# Dog: Woof!
# Cat: Meow!
# Animal: Some generic animal sound