import classes2 as c
print("********WELCOME TO LIBRARY AND INFORMATION CENTRE, CHAITANYA BHARATHI INSTITUTE OF TECHNOLOGY********")
print()
print(" 1.Add Student", "\n", "2.Issue Book", "\n", "3.Book return", "\n", "4.Display student information", "\n", "5.Display book information", "\n", "6.Add new book", "\n", "7.Clear fine")
n=int(input("Please enter your choice: "))
while n!=-1:
    if n == 1:
        c.addstudent()
    elif n == 2:
        c.issuebook()
    elif n == 3:
        c.returnbook()
    elif n == 4:
        c.displaystudentinfo()
    elif n == 5:
        c.displaybookinfo()
    elif n == 6:
        c.addbook()
    elif n == 7:
        c.clearfine()
    else:
        print("Entered wrong choice")
    n = int(input("Enter your choice from 1-6 (Enter(-1) to exit: "))
    print()
print("LIBRARY CLOSED")





