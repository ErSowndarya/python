#Set:
#Donot allow duplicate.
#duplicate values will be removed
#any datatypes allowed
#We cannot modify the items,
#we can add or remove items,
#unordered
#add(), update(), remove(), pop()

chocolateSet={"diaryMilk", "kitKat","fiveStar"}
print(type(chocolateSet))
#add the elements
chocolateSet.add("milkyBar")
#delete the elements
#unordered setp
chocolateSet.pop()
print(chocolateSet)
chocolateSet.add("true")
chocolateSet.add(True)
print(chocolateSet)

#Donot allow duplicate. because bool true and integer 1 value are same
chocolateSet.add(1)
print(chocolateSet)

chocolateSet.update("test one")
print(chocolateSet)

