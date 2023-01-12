import string
import random


class VehicleRegistry:

    def generate_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_lisence_plate(self, id):
        return f"{id}-{''.join(random.choices(string.digits, k=3))}"

class CarApplication:
    def register_vehicle(self, brand_name: string):
        #(1) create an instance of VechileRegistery
        registry = VehicleRegistry()

        #(2) generate a vechile id
        vehicle_id = registry.generate_id(3)

        #(3) generate the vehicle lisence plate
        lisence_plate = registry.generate_lisence_plate(vehicle_id)

        #(4) compute the catolgue price
        catalogue_price = 0
        if brand_name == "Tesla Model 3":
            catalogue_price = 6000
        elif brand_name == "VolksWagen ID3":
            catalogue_price = 3500
        elif brand_name == "BMW 5":
            catalogue_price = 45000

        #(5) compute the tax percentage, default is 0.05 except for electric cars it goes down in the tax %
        tax_percentage = 0.05
        if brand_name in ("Tesla Model 3", "VolksWagen ID3"):
            tax_percentage = 0.02
        
        payable_tax = tax_percentage * catalogue_price

        #(6) print the vechile registration info
        print("Registeration Complete! Your vehicle Information is:")
        print("brand: ",brand_name)
        print("ID: ",vehicle_id)
        print("Lisence plate: ",lisence_plate)
        print("Price: ", catalogue_price)
        print("Payable Tax: ",payable_tax)


car_app = CarApplication()
car_app.register_vehicle("VolksWagen ID3")

