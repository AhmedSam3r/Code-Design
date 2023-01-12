import string
import random

#Same meaning as CarInfo or BrandInfo or Vechile Info
class ModelInfo:
    name: str
    price: int
    is_electric: bool

    def __init__(self, name, price, is_electric) -> None:
        self.name = name
        self.price = price
        self.is_electric = is_electric
    
    def compute_tax(self) -> int:
        #(5) compute the tax percentage, default is 0.05 except for electric cars it goes down in the tax %
        tax_percentage = 0.05
        if self.is_electric:
            tax_percentage = 0.02

        return tax_percentage

    def calculate_tax(self) -> float:
        return self.compute_tax() * self.price

    def print(self) -> None:
        print("Model name: ",self.name)
        print("Price: ", self.price)
        print("Payable Tax: ",self.calculate_tax())



class Vehicle:
    id: str
    lisence_plate: str
    vehicle_info: ModelInfo

    def __init__(self, id, lisence_plate, vehicle_info) -> None:
        self.id = id
        self.lisence_plate = lisence_plate
        self.vehicle_info = vehicle_info

    def print(self) -> None:
        print("ID: ",self.id)
        print("Lisence plate: ",self.lisence_plate)
        self.vehicle_info.print()



class VehicleRegistry:
    model_info = {}

    def add_model_info(self, model_name, price, is_electric):
        self.model_info[model_name] = ModelInfo(model_name, price, is_electric)
    
    def __init__(self) -> None:
        #TODO replace it with info from DB car table
        self.add_model_info("VolksWagen ID3", 1000, True)
        self.add_model_info("Tesla Model 3", 10000, True)
        self.add_model_info("BMW 5", 100000, False)

    def generate_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_lisence_plate(self, id):
        return f"{id}-{''.join(random.choices(string.digits, k=3))}"

    def create_vehicle(self, model_name):
        #(2) generate a vechile id
        vehicle_id = self.generate_id(3)
        #(3) generate the vehicle lisence plate
        lisence_plate = self.generate_lisence_plate(vehicle_id)
        return Vehicle(vehicle_id, lisence_plate, self.model_info[model_name])


class VehicleApplication:
    def register_vehicle(self, model_name: string):
        #(1) create an instance of VechileRegistery
        registry = VehicleRegistry()

        #create a vehicle (new)
        vehicle = registry.create_vehicle(model_name)

        return vehicle        


vehicle_app = VehicleApplication()
#TODO make naming as input to the user where they first select the name
vehicle = vehicle_app.register_vehicle("VolksWagen ID3")

print("Registeration Complete! Your vehicle Information is:")
vehicle.print()

