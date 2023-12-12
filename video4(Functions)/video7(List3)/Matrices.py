PrintRowVice=[]
MatricesOfNumberA=[1,2,3]
MatricesOfNumberB=[4,5,6]
MatricesOfNumberC=[7,8,9]
PrintRowVice.append(MatricesOfNumberA)
PrintRowVice.append(MatricesOfNumberB)
PrintRowVice.append(MatricesOfNumberC)
print(PrintRowVice)
for row in PrintRowVice:
    for column in row:
        print(column,end="")
    print()
