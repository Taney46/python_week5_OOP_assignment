class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self.power_level = power_level
    
    def display_identity(self):
        return f"{self.alias}, also known as {self.name}, is here to save the day!"
    
    def use_power(self):
        return f"{self.alias} uses their superpower! Power level: {self.power_level}"
    
# Inherited class 
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        super().__init__(name, alias, power_level)
        self.__flight_speed = flight_speed  # Encapsulation: private attribute

    def use_power(self):
        return f"{self.alias} flies through the sky at {self.__flight_speed} km/h with a power level of {self.power_level}!"

    def set_flight_speed(self, speed):
        self.__flight_speed = speed

    def get_flight_speed(self):
        return self.__flight_speed

# Create objects instances
hero = Superhero("Bruce Wayne", "Batman", 85)
flyer = FlyingSuperhero("Clark Kent", "Superman", 100, 1200)

# Access attributes and methods
print(hero.display_identity())
print(hero.use_power())

print(flyer.display_identity())
print(flyer.use_power())

# Using encapsulated methods
flyer.set_flight_speed(1500)
print(f"New flight speed: {flyer.get_flight_speed()} km/h")
