#Take the following inputs from the HR officer:
#Employee’s day of joining (an integer between 1 and 31)
#Employee’s month of joining (‘JAN’, ‘FEB’, ‘MAR’, ‘APR’, … etc.)
#Employee’s year of joining
#Employee’s monthly salary after TDS 
day=int(input("Enter day of joining:"))
month=input("Enter month of joining:('Jan','February','march','april','may'):")
year=int(input("Enter year of joining:"))
salary=int(input("Employee monthly salary after TDS"))
pay=0
if month=="jan" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="December":
    Number=31
elif month=="april" or month=="june" or month=="september" or month=="november":
    Number=30
elif month=="february":
    if year%400==0:
        Number=29
    elif year%100==0:
        Number=28
    elif year%4==0:
        Number=29
    else:
        Number=28
pay = salary * (((Number-day) + 1) / Number)
print("Salary of the Employee is",round(pay))