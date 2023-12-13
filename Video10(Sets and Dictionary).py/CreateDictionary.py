#In dictionary and key value pair does not matter because in the dictionary data structure we are basically
#optimizing for search, not maintaining order or not others.
#Sets and dictionary -unordered


#Creating a Dictionary
CreateADictionary={"sowndaryatamizharasi@gmail":2567,"sowndaryadcareer@gmail":8055,"sowndaryad20@gmail":1067,0:5}
ChangeTheValue="sowndaryad20@gmail"
#Change a value
CreateADictionary[ChangeTheValue]=4444
#Creating a new email id

#When change a email id it creates a new key value pairs, can't ,modify a key 
#Only create new key value pairs


CreateANewEmail="sownd@gmail"
CreateADictionary[CreateANewEmail]=4444



print(CreateADictionary)




print(CreateADictionary[ChangeTheValue])

print(type(CreateADictionary))
print(CreateADictionary)
print(CreateADictionary['sowndaryad20@gmail'])
print(CreateADictionary["sowndaryadcareer@gmail"])
print(CreateADictionary[0])

