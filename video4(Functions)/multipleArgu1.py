#Returning multiple values from a function:

#fuction definition
def divide(A,B):
    return int(A//B),int(A%B)
#call the function
A,B=divide(17,2)
print(A,B)