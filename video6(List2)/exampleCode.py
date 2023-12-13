

#example code

LengthOfOutput = list(input())

for x in range(len(LengthOfOutput)):
  if LengthOfOutput[x] != " ":
    print(LengthOfOutput[x])
  else:
    LengthOfOutput.remove(" ")
  print(LengthOfOutput)



print(LengthOfOutput)


