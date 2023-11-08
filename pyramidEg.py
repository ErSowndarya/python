print("pyramid:")
column=1

while column<=5:
    row=1
    while row<=column:
        print(row,end= "")
        row+=1
    print()
    column+=1
    
print()

print("Reverse pyramid:")
column=5

while column>=1:
    row=5
    while row>=column:
        print(row,end= "")
        row-=1
    print()
    column-=1
    
print()
