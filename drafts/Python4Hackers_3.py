# Write a program that prompts user to enter their score out of 100 and displays their grade
# >= 90: A,80-89: B, 70-79: C, 60-69:D, <60: F
grade = int(input("What is your grade out of 100? ")) 

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

