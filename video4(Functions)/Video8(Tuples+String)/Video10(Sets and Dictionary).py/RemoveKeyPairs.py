#removing Elements
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

print(CreateADictionary)    