#Index of Elements
#index of elements always starts from 0

PrintIndexofElements=[2,8,56,8,3]

#Replace the index
PrintIndexofElements[0]="Sowndarya"
PrintIndexofElements[4]=45

#Length of PrintIndexOfElements
print(len(PrintIndexofElements))

#print index of 3
print(PrintIndexofElements[3])  

#printing last elements
print(PrintIndexofElements[4])

#index of -1 reverse direction will work
print(PrintIndexofElements[-1])
print(PrintIndexofElements[-5])
print(PrintIndexofElements)


#list index out of range because index 5 is not defined
print(PrintIndexofElements[5])