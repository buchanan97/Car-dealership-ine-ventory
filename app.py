class Vehicle:
    def __init__(self, description, price, color, mileage):
        self.description = description
        self.price = price
        self.color = color
        self.mileage = mileage

class Inventory:
    def __init__(self):
        self.vehicles = {
            'Honda Luxury': Vehicle('This is the Honda Luxury vehicle', 50000, 'Black', 20000),
            'Honda Sports': Vehicle('This is the Honda Sports vehicle', 35000, 'Red', 15000),
            'Honda Hybrid SportSE': Vehicle('This is the Honda Hybrid SportSE vehicle', 45000, 'Blue', 18000),
            'Toyota Corolla': Vehicle('This is the Toyota Corolla vehicle', 25000, 'White', 10000)
        }
    
    def get_vehicle(self, vehicle_type):
        if vehicle_type in self.vehicles:
            return self.vehicles[vehicle_type]
        else:
            return None
# Create an instance of the Inventory class
inventory = Inventory()

# Get input from the user
print("welcome to the Car delearship")
vehicle_type = input("What type of vehicle are you looking for? ")

# Get the vehicle object from the inventory
vehicle = inventory.get_vehicle(vehicle_type)

# Print the vehicle details
if vehicle is not None:
    print(vehicle.description)
    print('Price:', vehicle.price)
    print('Color:', vehicle.color)
    print('Mileage:', vehicle.mileage)
else:
    print("Sorry, we don't have that vehicle in our inventory.")