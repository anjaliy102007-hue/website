class vehicle:
    def __init__(self,name,number,model):
        self.name = name
        self.number = number
        self.model = model
        self.available = True

    def __str__(self):
        return self.name + " " + self.model
    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle not available")
    def return_vehical(self):
        self.available = True
        print("Vehical returned successfully")

class customer:
    def __init__(self,name):
        self.name = name
        self.__vehicles = []

    def rent_vehicle(self,v):
        if v.available:
            v.rent()
            self.__vehicles.append(v)
        else:
            print("Not available")

    def return_vehicle(self,v):
        if v in self.__vehicles:
            v.return_vehicle()
            self.__vehicles.remove(v)

    def __len__(self):
        return len(self.__vehicles) 

    class Rentalshop:
        def __init__(self):
            self.vehicles = []

        def add_vehicle(self,v):
            self.vehicles.append(v)

# create vehicle
v1 = vehicle("car","123","Porsche")   
v2 = vehicle("car","124","Jaguar")  
v3 = vehicle("Bike","125","Bullet")    
v4 = vehicle("car","126","Pulsar")        
v5 = vehicle("car","127","BMW")           

# create RentalShop class
class RentalShop:
    def __init__(self):
     self.vehical = []

    def add_vehicle(self,v):
     self.vehical.append(v)

shop = RentalShop()

shop.add_vehicle(v1)
shop.add_vehicle(v2)
shop.add_vehicle(v3)
shop.add_vehicle(v4)
shop.add_vehicle(v5)

# create customer
c1 = customer("Anjali")
c2 = customer("Avi")

# rent vehicle
c1.rent_vehicle(v1)
c2.rent_vehicle(v2)

# count vehicles
print("Anjali rented:",len(c1))
print("Avi rented:",len(c2))

# Return vehicle
c1.rent_vehicle(v1)

# Display vehicle
print(v1) 