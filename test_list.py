#A python program to test on list properties

#prompt the user to enter the list of names
employee_list=[]
#use a for loop to instruct the user to enter the the six number of employee name
for i in range(6):
    name=input("enter employee name:")
    employee_list.append(name)
#to print the list for employee's name    
print(employee_list)    
#convert the list to set to remove dublicates
unique_employee_list=list(set(employee_list))
#output of employee name without dublicate
print("Employee's names without dublicates: ")
for name in unique_employee_list:
    print(name)

#to sort the names with alphabetical order
unique_employee_list.sort()

#display names after being sorted
print("Sorted list of unique employee list: ")
for name in unique_employee_list:
    print(name)
#display the total number of names the user has entered
    
print("the total number of name in the list is: ",len(employee_list))   
