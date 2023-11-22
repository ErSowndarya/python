#Which of the following statements about the insert() method of a list is incorrect?
#A) A new element can be inserted of the beginning of a list----TRUE

InsertElementInBeginning=[1,2,3]
print(InsertElementInBeginning)
InsertElementInBeginning.insert(0,77)
print(InsertElementInBeginning)

#B)Another list can be inserted as a new element----TRUE
NewElementAdded=[1,2,4]
print(NewElementAdded)
NewElementAdded.insert(0,[88,89])
print(NewElementAdded)
 
#C)Any number of new elements can be passed as arguments--FALSE
PassedThreeArgumentsInList=[1,2,3,4]
PassedThreeArgumentsInList.insert(2,56,67)
print(PassedThreeArgumentsInList)

#3RD STATEMENT GOT ERROR BECAUSE INSERT EXPECTED ONLY 2 ARGUMENTS BUT IN THE LIST 3ARGUMENTS PASSED
