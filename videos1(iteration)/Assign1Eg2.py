#Take the marks of a student in an exam (out of 150), and print the grade achieved in that exam in the exact format shown in the example below

#Grading policy:

#0 to 50 -> C grade
#51 to 75 -> B grade
#76 to 120 -> A grade
#121 to 150 -> S grade
#Any other integer entered: WHAT????


marks=int(input("Enter marks in the exam:"))

if(marks<=50):
    print("C grade")
elif(marks<=75 and marks>=51):
    print("B grade")
elif(marks>=76 and marks<=120):
    print("A grade")
elif(marks>=121 and marks<=150):
    print("S grade")
else:
    print("Invalid")
