#Assume that the Delhi government had restarted the “odd-even” rule for vehicles. 
#Vehicles with numbers ending with an even digit may only drive their vehicles in the city, 
#if the day of the month is an even number. Odd numbered vehicles may only go out on odd numbered days.

#Ask the user to enter the last 4 integer digits of their vehicle number, 
#as well as the day of the month (1 to 31). Tell them if it’s safe to take your vehicle out or not.

vehicle=int(input("Enter last digits of the vehicle number:"))
month=int(input("Enter day of the month(1-31):"))
#this another type if(vehicle%2)==(month%2):
if(vehicle%2==0 and month%2==0):
    print("Take your vehicle out on this day!")
else:
    print("Do not take your vehicle out on this day!")

    