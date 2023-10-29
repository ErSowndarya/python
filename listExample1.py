#write a program to read 10numbers from the keyboard and find their sum
#store the num value one by one
a=[]
print("Enter 5 numbers")
#run a element from 1 to 5
for i in range(5):
#get the input to num
#For used casting(one datatype converted into another datatype)
    num=int(input("Enter num"+str(i+1)))
    #add the element in List
    a.append(num)
    #completing all the loop function to store elements in List
print(a)
#assign sum 
sum=0
# a value run one by one in i
for i in a:
    #add the elements sum and i
    sum=sum+i
    #after adding to got the sum value
print(sum)

