#A program to sum up the student subjects and give them a grade
#prompt the user to enter tthe mark of each subject
print("please enter your 3 marks")

num = 3

marks=[]
#using a for loop to  prompt the user to enter marks from 0-100
for i in range (num):
    aa=int(input("Enter your marks"+str(i)+":"))
    try:
        if 1<=aa<=100:
            marks.append(aa)
        else:
            print("input is out of range!!")
    except:
            print("input is no valid!!")
print(marks)

#calculate the sum and average
sumOfMarks = sum(marks)
average= sum(marks)/3

#display results
print("The sum of your marks is:"+str(sumOfMarks))
print(f"The average of your marks is:{average:.2f} ")

#Testing condition for grading
if average>=70 and 100:
    print("Grade  is A.")
elif average>=60 and 69:
    print("Grade  is B ")    
elif average>=50 and 59:
    print("Grade  is C")
elif average>=40 and 49:
    print("Grade is D")
elif average>=0 and 39:
    print("Grade  is Fail")
   
