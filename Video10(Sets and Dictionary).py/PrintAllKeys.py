CreateADictionary={"sowndaryatamizharasi@gmail":2567,"sowndaryadcareer@gmail":8055,"sowndaryad20@gmail":1067,0:5}


CreateANewEmail="sownd@gmail"
CreateADictionary[CreateANewEmail]=4444

#Key values added
print(CreateADictionary)
CreateADictionary['sownd123 delli@hotmail']= 9999
#Remove the elements
del CreateADictionary[0]

#another way removing the key values

X=CreateADictionary.pop('sownd123 delli@hotmail')
print(X, CreateADictionary)

#Printing all keys
print(CreateADictionary)    
for x in CreateADictionary.keys():
    print(x)

#Printing all values
for x in CreateADictionary.keys():
    print(X)

#Printing all Key-pairs/all items

for x in CreateADictionary.items():
    print(x)



for x,y in CreateADictionary.items():
    print(x,"has the value",y)

