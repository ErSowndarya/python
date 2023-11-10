#Returning multiple values from a function:

#fuction definition
def ReturnQuotientAndRemainderOfFunction(A,B):
    return int(A//B),int(A%B)
#call the function
A,B=ReturnQuotientAndRemainderOfFunction(17,2)
print(A,B)