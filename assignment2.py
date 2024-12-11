# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Create instances
vehicles = [Car(), Plane(), Boat()]

# Loop through and call the move() method
for vehicle in vehicles:
    print(vehicle.move())
