#How many uppercase and lowercase characters are present
LowerCaseUpperCaseCount='There was a BIG boy'
countU=0
countL=0
sp=0
for char in LowerCaseUpperCaseCount:
    if char.isupper():
        countU+=1
    elif char.islower():
        countL+=1
    else:
        sp+=1
print(countU,countL,sp)