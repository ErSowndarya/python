ReverseOrder = list(input())
for i in range(len(ReverseOrder)-1,0,-1):
        if ReverseOrder[i] != " ":
            print(ReverseOrder[i],end = " ")


print(ReverseOrder)