DeleteTheElements={1:100,2:100000}
#Using del- It does not return any value
del DeleteTheElements[1]
print(DeleteTheElements)

#Using Pop method
#Pop method: return values and delete the key 
X=DeleteTheElements.pop(2)
print(X,DeleteTheElements)