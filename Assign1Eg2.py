marks=int(input("Enter marks in the exam:"))
if(marks<=50):
    print("A grade")
elif(marks<=75 and marks>=51):
    print("B grade")
elif(marks<=121 and marks<=150):
    print("S grade")
else:
    print("Invalid")
