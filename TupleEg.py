#Tuple:
#Allows duplicate
#store any type of datatypes
#We cannot modify the tuple item

vegtablesTuple=("potato","drumstick","brinjal")
print(type(vegtablesTuple))
#Used Casting
vegtablesTuple1=list(vegtablesTuple)
print(type(vegtablesTuple1))
#add the elements in list
vegtablesTuple1.append("carrot")
#remove the elements
vegtablesTuple1.pop(3)
print(vegtablesTuple1)