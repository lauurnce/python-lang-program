class F1Car: #class definition
    racing_series = "Formula 1" #class variable
 
    def __init__(self, driver, team, car_model, engine): #constructor method, it defines the attributes of the class and initializes them when an object is created
        self.driver = driver #instance variable
        self.team = team 
        self.car_model = car_model
        self.engine = engine 
        
    def description(self): #instance method 
        return f"{self.driver} drives the {self.car_model} for {self.team}." #self is used to access the instance variables within the class
        #setting behavior of the class
    def race(self, action): 
        return f"The {self.team} car powered by {self.engine} {action}!"
    
car1 = F1Car("Max Verstappen", "Red Bull Racing", "RB20", "Honda RBPT") #car1 is the object or instance of the class F1Car
car2 = F1Car("Sergio Perez", "Red Bull Racing", "RB20", "Honda RBPT") #data type of object is class
car3 = F1Car("Lewis Hamilton", "Mercedes", "W15", "Mercedes") #car3 is an instance of the F1Car class with specific attributes for driver, team, car_model, and engine
car4 = F1Car("George Russell", "Mercedes", "W15", "Mercedes") #F1Car is the class, car4 is the instance of the class with specific attributes for driver, team, car_model, and engine
car5 = F1Car("Charles Leclerc", "Ferrari", "SF-24", "Ferrari")
car6 = F1Car("Carlos Sainz", "Ferrari", "SF-24", "Ferrari")
car7 = F1Car("Lando Norris", "McLaren", "MCL38", "Mercedes")
car8 = F1Car("Oscar Piastri", "McLaren", "MCL38", "Mercedes")
car9 = F1Car("Fernando Alonso", "Aston Martin", "AMR24", "Mercedes")
car10 = F1Car("Lance Stroll", "Aston Martin", "AMR24", "Mercedes")
print("--- Accessing Attributes ---")
print(car3.driver) #accessing instance variable
print(car3.racing_series)   
print("\n--- Calling Methods ---")
print(car3.description())  #accessing instance method which uses instance variables                    
print(car3.race("activates DRS on the straight"))
print(car5.description())  #car5 is object and description is the instance method                   
print(car5.race("sets the fastest lap"))       

#local variable or instance variable