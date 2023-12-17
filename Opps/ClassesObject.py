class bike:
    mileage = ""
    price =""
    model =""
    Engine =""

    def service():
        print("You have to service every 2000 KMs")

honda = bike
honda.mileage = "50Kmpl"

print(honda.mileage)
honda.service()

Hero = bike
Hero.mileage = "60Kmpl"
print(Hero.mileage)

suzuki = bike
suzuki.mileage = "45Kmpl"
print(suzuki.mileage)