#getting Rohith sharma Runs
RohithSharma=[]
x1=0
while(x1>=0):
    x1=int(input("Enter score in match:"))
    if x1<0:
        break
    RohithSharma.append(x1)
print(RohithSharma)
MSDhoni=[]
x1=0
while(x1>=0):
    x1=int(input("Enter score in match:"))
    if x1<0:
        break
    MSDhoni.append(x1)
print(MSDhoni)

RohithSharma_H=0
MSDhoni_H=0
for i in RohithSharma:
    if i>RohithSharma_H:
        RohithSharma_H=i

for i in MSDhoni:
    if i>MSDhoni_H:
        MSDhoni_H=i
if RohithSharma_H>MSDhoni_H:
    print("RohithSharma is better")
elif RohithSharma_H<MSDhoni_H:
    print("MSD is better")
else:
    print("Both are equal")
print(RohithSharma_H,MSDhoni_H)