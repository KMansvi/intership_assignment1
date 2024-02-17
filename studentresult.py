num=input("Enter the student number: ")
name=input("Enter the student name: ")
s1=int(input("Enter the marks in first subject: "))
s2=int(input("Enter the marks in second subject: "))
s3=int(input("Enter the marks in third subject: "))
avg=(s1+s2+s3)/3
if avg>=75:
    print("Student "+name+" with roll number "+num+" has passed with DISTINCTION")
elif avg>=60 and avg<75:
    print("Student "+name+" with roll number "+num+" has passed in FIRST CLASS")
elif avg>=50 and avg<60:
    print("Student "+name+" with roll number "+num+" has passed in SECOND CLASS")
elif avg>=35 and avg<50:
    print("Student "+name+" with roll number "+num+" has passed in THIRD CLASS")
else:
    print("Student "+name+" with roll number "+num+" has FAILED")
    
