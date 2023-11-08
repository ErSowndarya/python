#Ask the user to enter height in centimeters. Return the same height in feet and inches.
#Floating point values in the answer should be rounded up or down to the nearest integer
#”Optional” addition to your code:
#Add exception handling, in case the user enters an invalid input (use try… except statements, by referring to THIS article)


cm=float(input("Enter height in centimeters:"))
inches=0.394*cm
feet=0.328*cm
print("The entered height is equal to ",round(inches,2),"inches",round(feet,2),"feet")
