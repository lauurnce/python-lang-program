# Multilevel Inheritance Example in Python
# 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color 

    def give_birth(self):
        return f"{self.name} gives birth to live young"

class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

    def fetch(self):
        return f"{self.name} fetches the ball"

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy", "Brown", "Golden Retriever")
    print(dog.speak())  # Buddy barks
    print(dog.give_birth())  # Buddy gives birth to live young
    print(dog.fetch())  # Buddy fetches the ball
    print(f"{dog.name} has {dog.fur_color} fur and is a {dog.breed}")
