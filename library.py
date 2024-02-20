#A python program to calculate the fine for overdue library books

def library():
    bookID=int(input("Enter the student book ID:"))
    dueDate=int(input("Enter the student Due date(YYYY-MM-DD):"))
    returnDate=int(input("Enter the student return date(YYYY-MM-DD):"))
    daysOverdue=returnDate-dueDate
    print("days overdue:",daysOverdue)
    if daysOverdue <= 7:
        fineRate=20
        fineAmount=daysOverdue*fineRate
        print("fine Amount:",fineAmount)
    elif daysOverdue>=8 and daysOverdue<=14:
        fineAmount=daysOverdue*50
        print("fine Amount:",fineAmount)
    elif daysOverdue >15:
        fineAmount=daysOverdue*100
        print("fine Amount:",fineAmount)

library()
