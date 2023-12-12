PrintColumnVice=[]
MatricesOfNumberA=[1,2,3]
MatricesOfNumberB=[4,5,6]
MatricesOfNumberC=[7,8,9]
PrintColumnVice.append(MatricesOfNumberA)
PrintColumnVice.append(MatricesOfNumberB)
PrintColumnVice.append(MatricesOfNumberC)
print(PrintColumnVice)
for column in range (len(PrintColumnVice[1])):
    for row in range(len(PrintColumnVice)):
        print(PrintColumnVice[row][column],end="")
    print()
