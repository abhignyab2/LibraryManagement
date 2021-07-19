from datetime import *


class StudentInformation:
    def __init__(self, name, roll, branch, semester):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.semester = semester
        self.booksborrowed=[]
        self.book = None
        self.fine=0
	  

    def display(self):
        print( "STUDENT INFORMATION" )
        print( "Name: " , self.name)
        print( "Roll Number: ", self.roll)
        print( "Branch: ", self.branch)
        print( "Semester: ", self.semester)
        print( "Books borrowed till now: ", "\n", self.booksborrowed)
        print( "Code of book which is borrowed= ",self.book)
        print( "Fine : ", self.fine, "Rupees")
        print( "\n" )


student = []


class Book:
    def __init__(self, name, author, code, copies, magazine):
        self.name = name
        self.code = code
        self.author = author
        self.copies = copies
        self.magazine = magazine

    def display(self):
        print( "Name: ", self.name)
        print( "Author: ", self.author)
        print( "Book code= ", self.code)
        print( "No. of copies available: ", self.copies)
        print( "\n" )


book = []


def addstudent():
    """This function appends student information"""
    student.append(StudentInformation(input("Enter name: "), input("Enter roll: "), input("Enter branch: "), int(input("Enter semester: "))))
    print()


def displaystudentinfo():
    """This function displays information of all students"""
    for stu in student:
        stu.display()


def displaybookinfo():
    """This function displays the list of available books"""
    for bk in book:
        bk.display()


def addbook():
    """This function adds a new book"""
    book.append(Book(input("Enter name: "), input("Enter Author: "), input("Enter Code: "), int(input("Enter no. of copies: ")), input("Is it a magazine: ")))
    print()


def issuebook():
    """This function keeps a record of book isues"""
    flag = 1
    flag1=1
    bk1 = None
    book_code = input( "Enter book code: " )

    for bk in book:
        if bk.code == book_code:
            bk1=bk
            if bk.magazine == "Yes":
                print("You cannot borrow a magazine")
                return
                flag = 0
            if bk.copies == 0:
                print( "No more copies of the book available: " )
                return

    if flag == 1:
        print( "No such book available" )
        return

    stu_roll = input( "Enter student roll number:  " )

    for stu in student:
        if stu.roll == stu_roll:
            flag1=0
            if stu.book:
                print( "You can borrow only one book at a time!" )
                return
            else:
                stu.book = book_code
                d,m,y = map(int,input( "Issue date in form of dd/mm/yyyy").strip().split("/"))
                stu.is_date=date(y,m,d)
                bk1.copies-=1
                stu.ret_date=stu.is_date+timedelta(days=7)
                stu.booksborrowed.extend({bk1.name,":",(stu.is_date).strftime("%d %B %Y")})
                print( "Details of book you have borrowed: " )
                print(bk1.display())
                print( "\n", "Return book on or before ", (stu.ret_date).strftime("%d %B %Y"), "\n")

    if flag1 == 1:
        print( "Wrong roll number!" )
        print()


def returnbook():
    """This function keeps the record of returned books"""
    stu_roll = input( "Enter student roll number: " )
    book_code = None

    for stu in student:
        if stu.roll == stu_roll:
            if stu.book:
                book_code = stu.book
                d,m,y = map(int,input( "Enter return date in form of dd/mm/yyyy: ").strip().split("/"))
                r_date = date(y,m,d)
                nodays = (r_date-stu.is_date).days
                if nodays > 7:
                    print( "You have to pay a fine of ", nodays-7, "Rupees")
                    stu.fine += nodays-7
                stu.book = None
            else:
                print( "You have borrowed no books" )
                return

    for bk in book:
        if bk.code == book_code:
            bk.copies += 1

    print()

def clearfine():
    """This function is for keeping record of fine payment"""
    roll_no = input( "Enter roll number: " )

    for stu in student:
        if stu.roll == roll_no:
            if stu.fine!=0:
                print( "You have to pay a fine of ", stu.fine, "Rupees" )
                n = int(input( "Enter the amount you want to pay: " ))
                stu.fine -= n
                if stu.fine !=0 :
                    print( "You have to pay a fine of " , stu.fine, "Rupees" )
                else:
                    print( "Your dues are cleared" )
            else:
                print( "You have no fine" )
                    

