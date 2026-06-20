class Vehical:
    def __init__(self, Vehicalnumber, owner_name, parking_hour):
        self.vehical_no = Vehicalnumber
        self.ownername = owner_name
        self.parkinghours = parking_hour

    def caluclate_bill(self):
        return 0


class Car(Vehical):
    def caluclate_bill(self):
        return self.parkinghours * 30


class Bike(Vehical):
    def caluclate_bill(self):
        return self.parkinghours * 15


class Truck(Vehical):
    def caluclate_bill(self):
        return self.parkinghours * 50


n = int(input())

Vehicals = []
total = 0
max_bill = 0
max_vehiclas = None

for i in range(n):
    Vehical_type = input().lower()
    Vehicalnumber = input()
    owner_name = input()
    parking_hour = int(input())

    if Vehical_type == "car":
        v = Car(Vehicalnumber, owner_name, parking_hour)

    elif Vehical_type == "bike":
        v = Bike(Vehicalnumber, owner_name, parking_hour)

    elif Vehical_type == "truck":
        v = Truck(Vehicalnumber, owner_name, parking_hour)

    else:
        print("Invalid vehicle type")
        continue

    Vehicals.append(v)

    bill = v.caluclate_bill()
    total += bill

    if bill > max_bill:
        max_bill = bill
        max_vehiclas = v


print("Total Collection =", total)

if max_vehiclas:
    print("Highest Bill Vehicle:")
    print("Vehicle No =", max_vehiclas.vehical_no)
    print("Owner Name =", max_vehiclas.ownername)
    print("Bill =", max_bill)
     
    




