# Hybrid Inheritance Example in Python
# Hybrid inheritance combines multiple inheritance with other inheritance types
# This example demonstrates a diamond inheritance structure with detailed variable explanations

class Animal:
    # Class variable: shared by all instances of Animal and its subclasses
    # This variable is stored in the class namespace, not instance namespace
    kingdom = "Animalia"  # Class variable - same for all animals

    def __init__(self, name, species):
        # Instance variables: unique to each instance
        # These are stored in the instance's __dict__
        self.name = name        # Instance variable - each animal has its own name
        self.species = species  # Instance variable - each animal has its own species
        print(f"Animal.__init__ called: name={name}, species={species}")

    def breathe(self):
        # Instance method that can access both class and instance variables
        return f"{self.name} ({self.species}) is breathing in the {self.kingdom} kingdom"

class Mammal(Animal):
    # Class variable specific to Mammal class
    # This shadows the parent class variable for Mammal and its subclasses
    has_fur = True  # Class variable - all mammals have fur

    def __init__(self, name, species, fur_color):
        # Call parent class __init__ to initialize inherited instance variables
        super().__init__(name, species)
        # Additional instance variable for Mammal
        self.fur_color = fur_color  # Instance variable - each mammal has its own fur color
        print(f"Mammal.__init__ called: fur_color={fur_color}")

    def nurse_young(self):
        # Instance method accessing instance variables
        return f"{self.name} nurses its young with {self.fur_color} fur"

class Bird(Animal):
    # Class variable specific to Bird class
    can_fly = True  # Class variable - most birds can fly

    def __init__(self, name, species, wingspan):
        # Call parent class __init__
        super().__init__(name, species)
        # Instance variable for Bird
        self.wingspan = wingspan  # Instance variable - each bird has its own wingspan
        print(f"Bird.__init__ called: wingspan={wingspan}")

    def fly(self):
        # Instance method accessing instance variables
        return f"{self.name} flies with a {self.wingspan} cm wingspan"

class Bat(Mammal, Bird):
    # Class variable for Bat - this is hybrid inheritance (multiple + single)
    nocturnal = True  # Class variable - bats are nocturnal

    def __init__(self, name, species, fur_color, wingspan, echolocation_range):
        # For hybrid inheritance with diamond problem, we need to be careful with initialization
        # We'll initialize the common Animal part first, then the specific parts
        Animal.__init__(self, name, species)  # Initialize the shared base class once
        # Now initialize the specific attributes for each inheritance path
        self.fur_color = fur_color  # Instance variable from Mammal path
        self.wingspan = wingspan    # Instance variable from Bird path
        self.echolocation_range = echolocation_range  # Instance variable specific to Bat
        print(f"Bat.__init__ called: fur_color={fur_color}, wingspan={wingspan}, echolocation_range={echolocation_range}")

    def navigate_darkness(self):
        # Instance method accessing variables from multiple inheritance paths
        return f"{self.name} uses echolocation up to {self.echolocation_range}m to navigate"

# Example usage demonstrating hybrid inheritance
if __name__ == "__main__":
    print("=== Creating a Bat instance ===")
    bat = Bat("Bruce", "Microchiroptera", "Black", 30, 50)

    print("\n=== Accessing Class Variables ===")
    print(f"Kingdom (from Animal class): {bat.kingdom}")        # Accessed via instance
    print(f"Has fur (from Mammal class): {bat.has_fur}")        # Accessed via instance
    print(f"Can fly (from Bird class): {bat.can_fly}")          # Accessed via instance
    print(f"Nocturnal (from Bat class): {bat.nocturnal}")       # Accessed via instance

    print("\n=== Accessing Instance Variables ===")
    print(f"Name: {bat.name}")                                  # Instance variable
    print(f"Species: {bat.species}")                            # Instance variable
    print(f"Fur color: {bat.fur_color}")                        # Instance variable from Mammal
    print(f"Wingspan: {bat.wingspan}")                          # Instance variable from Bird
    print(f"Echolocation range: {bat.echolocation_range}")      # Instance variable from Bat

    print("\n=== Calling Methods ===")
    print(bat.breathe())         # Method from Animal
    print(bat.nurse_young())     # Method from Mammal
    print(bat.fly())            # Method from Bird
    print(bat.navigate_darkness())  # Method from Bat

    print("\n=== Method Resolution Order (MRO) ===")
    print(f"MRO: {Bat.__mro__}")  # Shows the inheritance resolution order
