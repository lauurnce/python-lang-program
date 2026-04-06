class F1Car: # Class definition
    racing_series = "Formula 1" # Class variable: Same for EVERY car
 
    # Constructor: Initializes attributes when an object is created
    def __init__(self, driver, team, car_model, engine): 
        self.driver = driver # Instance variable: Unique to this specific car
        self.team = team 
        self.car_model = car_model
        self.engine = engine 
        
    # Instance method: Uses 'self' to access instance variables
    def description(self): 
        return f"{self.driver} drives the {self.car_model} for {self.team}." 
        
    # Instance method defining a behavior
    def race(self, action): 
        return f"The {self.team} car powered by {self.engine} {action}!"
    
# Creating Instances (Objects) of the F1Car class
car3 = F1Car("Lewis Hamilton", "Mercedes", "W15", "Mercedes") 
car5 = F1Car("Charles Leclerc", "Ferrari", "SF-24", "Ferrari")

print("--- Accessing Attributes ---")
print(car3.driver) # Accessing instance variable (Lewis Hamilton)
print(car3.racing_series) # Accessing class variable (Formula 1)

print("\n--- Calling Methods ---")
print(car3.description())                   
print(car5.race("sets the fastest lap"))
