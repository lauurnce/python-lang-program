# Hierarchical Inheritance Example in Python
# Hierarchical inheritance occurs when multiple classes inherit from a single base class
# This creates a tree-like structure where one parent has multiple children

class Vehicle:
    vehicle_count = 0  # Class variable 

    def __init__(self, make, model, year):
        self.make = make      # Instance variable 
        self.model = model   
        self.year = year      
        Vehicle.vehicle_count += 1  # Modify class variable through class name
        print(f"Vehicle.__init__ called: {make} {model} ({year})")

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine is starting"

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine is stopping"

    @classmethod
    def get_vehicle_count(cls):
        return f"Total vehicles created: {cls.vehicle_count}"

class Car(Vehicle):
    wheels = 4 

    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors        
        self.fuel_type = fuel_type 
        print(f"Car.__init__ called: doors={doors}, fuel_type={fuel_type}")

    def drive(self):
        return f"Driving the {self.year} {self.make} {self.model} ({self.doors} doors, {self.fuel_type})"

    def honk(self):
        return f"The {self.make} {self.model} honks: Beep beep!"

class Truck(Vehicle):
    wheels = 6 

    def __init__(self, make, model, year, payload_capacity, towing_capacity):
        # Call parent class __init__
        super().__init__(make, model, year)
        # Instance variables specific to Truck
        self.payload_capacity = payload_capacity  
        self.towing_capacity = towing_capacity    
        print(f"Truck.__init__ called: payload={payload_capacity}t, towing={towing_capacity}t")

    def haul_cargo(self):
        return f"The {self.make} {self.model} is hauling {self.payload_capacity} tons of cargo"

    def tow_vehicle(self):
        return f"The {self.make} {self.model} can tow up to {self.towing_capacity} tons"

class Motorcycle(Vehicle):
    wheels = 2  

    def __init__(self, make, model, year, engine_cc, has_sidecar):
        super().__init__(make, model, year)
        self.engine_cc = engine_cc      
        self.has_sidecar = has_sidecar 
        print(f"Motorcycle.__init__ called: engine={engine_cc}cc, sidecar={has_sidecar}")

    def wheelie(self):
        return f"The {self.make} {self.model} ({self.engine_cc}cc) does a wheelie!"

    def check_sidecar(self):
        sidecar_status = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"The {self.make} {self.model} is {sidecar_status}"

# demonstrating hierarchical inheritance
if __name__ == "__main__":
    print("=== Creating Vehicle Instances ===")

    # Create a Car instance
    car = Car("Toyota", "Camry", 2023, 4, "Gasoline")
    print()

    # Create a Truck instance
    truck = Truck("Ford", "F-150", 2022, 1.5, 5.0)
    print()

    # Create a Motorcycle instance
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 1200, False)
    print()

    print("=== Accessing Class Variables ===")
    print(f"Vehicle count (class variable): {Vehicle.get_vehicle_count()}")
    print(f"Car wheels (class variable): {car.wheels}")
    print(f"Truck wheels (class variable): {truck.wheels}")
    print(f"Motorcycle wheels (class variable): {motorcycle.wheels}")
    print()

    print("=== Accessing Instance Variables ===")
    print(f"Car: {car.make} {car.model} ({car.year}) - {car.doors} doors, {car.fuel_type}")
    print(f"Truck: {truck.make} {truck.model} ({truck.year}) - {truck.payload_capacity}t payload, {truck.towing_capacity}t towing")
    print(f"Motorcycle: {motorcycle.make} {motorcycle.model} ({motorcycle.year}) - {motorcycle.engine_cc}cc, sidecar: {motorcycle.has_sidecar}")
    print()

    print("=== Calling Inherited Methods ===")
    print(car.start_engine())
    print(truck.start_engine())
    print(motorcycle.start_engine())
    print()

    print("=== Calling Specific Methods ===")
    print(car.drive())
    print(car.honk())
    print()
    print(truck.haul_cargo())
    print(truck.tow_vehicle())
    print()
    print(motorcycle.wheelie())
    print(motorcycle.check_sidecar())
    print()

    print("=== Demonstrating Polymorphism ===")
    # All vehicles can call the same method name, but behavior differs
    vehicles = [car, truck, motorcycle]
    for vehicle in vehicles:
        print(vehicle.start_engine())
    print()

    print("=== Class Hierarchy Information ===")
    print(f"Car MRO: {Car.__mro__}")
    print(f"Truck MRO: {Truck.__mro__}")
    print(f"Motorcycle MRO: {Motorcycle.__mro__}")
