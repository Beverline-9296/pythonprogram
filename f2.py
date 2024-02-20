"""import math
print("floor 1.3 is:",math.floor(1.3))
print("ceil 1.3 is:",math.ceil(1.3))
a=10
b=6
c=a//b
d=a/b
print("floor division (//)",c)
print("normal division(/)",d)
a=10
b=6
e=a%b
print("modulous (%)",e)



# divisibility test of a number
num=int(input("Enter a number:"))
if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

# a program to compile a discount

amount=float(input("enter amount of purchase"))
if amount >1000:
    discount =0.05*amount
    print("The discount is:",discount)
else:
    print("no discount")

#the grade
score=int(input("Enter your score:"))
if score>=90 and score<=100:
    print("Grade=A")
else:
    print("no grade")

#logical opperators

age=int(input("Enter your age:"))
income=int(input("Enter your income:"))
if age>=21 and income>=21000:
     print("CONGRATULATIONS YOU ARE QUALIFIED FOR A LOAN")
else:
    print("UNFOUTINATELY,WE ARE UNABLE TO OFFER YOU A LOAN AT THIS TIME")
     
 
a=10
b=5
print(a=10)


eastafrica=("Kenya","Uganda","Tanzania")
age=int(input("Enter your age:"))
country =input("enter your country:")
if age>18 and country is eastafrica:
     print("Eligible to vote")
else:
    print("Not eligible to vote")



a=[10,20]
b=a
b+=[30,40]
print(a)
print(b)


a=4
b=1
print(a|b)
print(a>>2)

print(2%6)


print(bool(0),bool(3.14),bool(-3),bool(1.0+1j))

print(2**3**2)


print(2*3**3*4)



#list
t=(1,2,4,3)
t=[1,3]
print (t)

list=['h','e','l','l','0']
print(len(list))


list1=[1,5,9]
print(sum(list1))


nums=set([1,1,2,3,3,3,4,4])
print(len(nums))

list1=[2,33,222,14,25]
print(list1[-1])

t=(1,2,4,3,8,9)
print([t[i]for i in range(0,len(t),2)])


a = [5,5,6,7,7,7]
b = set(A. def test(lst)
    if lst in b:
        return 1
    else:
        return 0
for i in  filter(test, A.:
    print(iend=" ")
    
t=(1,2,4,3)
print([1,-1])
list=[1,2,3,110]
print(max(list))

list1=[1,33,222,14,25]
print(list1[:-1])

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

def main():
    # Prompt user to enter marks for three subjects
    subject1 = float(input("Enter marks for Subject 1: "))
    subject2 = float(input("Enter marks for Subject 2: "))
    subject3 = float(input("Enter marks for Subject 3: "))

    # Calculate average score
    average = (subject1 + subject2 + subject3) / 3
    # Determine the grade based on the average score
    grade = calculate_grade(average)

    # Display the grade and the average marks of the student
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

main()"""


print("please enter your 5 marks")

num = 3
marks = []
for i in range(num):
    aa = int(input("enter mark"+str(i)+":"))
    try:
        if 1 <= aa <= 100:
            marks.append(aa)
        else:
            print("Input is out of range!")
    except:
        print('Input is not valid!')

print(marks)

#calculate the sum and average
sumOfMarks = sum(marks)
averageOfMarks = sum(marks)/5

#display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))










