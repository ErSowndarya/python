
#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
#Iterate through each command in order and perform the corresponding operation on your list.

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#print
#pop
#reverse
#print
if __name__ == '__main__':
    N = int(input())
    ListOfElements=[];
    for i in range(0,N):
        Index=input().split();
        if Index[0] == "insert":
            ListOfElements.insert(int(Index[1]),int(Index[2]))
        elif Index[0] == "append":
            ListOfElements.append(int(Index[1]))
        elif Index[0] == "pop":
            ListOfElements.pop();
        elif Index[0] == "print":
            print(ListOfElements)
        elif Index[0] == "remove":
            ListOfElements.remove(int(Index[1]))
        else:
            ListOfElements.reverse();