#example code 2

PrintReverseNumber = list(input())
B = []

for x in range(len(PrintReverseNumber)):
  if PrintReverseNumber[x] != " ":
    B.append(PrintReverseNumber[x])
  #print(A)
  #print(B)

for y in range(len(B)-1,0,-1):
  print(B[y], end= " ")


#print("Finally:", A, B)