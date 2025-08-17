import mysql.connector as msq
import random
import sys

mydb = msq.connect(host="localhost", user="root", passwd="123")
c = mydb.cursor()

c.execute("create database Library_Management_System")
c.execute("use Library_Management_System") 

c.execute("CREATE TABLE customer_details(C_id integer, C_Name varchar(15),\
Ph_no varchar(10), Book_issued integer, Issue_date varchar(12), Return_Date varchar(12), Member char(1), membership int(5))") 

c.execute("create table book_details(b_id int(5),b_name varchar(25),publication varchar(50),\
author varchar(15), status varchar(20),reviews decimal(5,3))") 

books = [
    (1, 'Convenience Store Woman', 'Knopf', 'Nicholas D', 'available', 4.0),
    (2, 'The Great Gatsby', 'Scribner', 'Scott Fitz', 'available', 4.5),
    (3, 'To Kill a Mockingbird', 'Lippincott & Co.', 'Harper Lee', 'available', 4.8),
    (4, '1984', 'Secker & Warburg', 'George Orwell', 'available', 4.7),
    (5, 'Pride and Prejudice', 'T. Egerton', 'Jane Austen', 'available', 4.6),
    (6, 'Moby Dick', 'Harper & Brothers', 'Herman Melville', 'available', 4.2),
    (7, 'War and Peace', 'The Russian Messenger', 'Leo Tolstoy', 'available', 4.4),
    (8, 'The Catcher in the Rye', 'Little, Brown and Company', 'J.D. Salinger', 'available', 4.3),
    (9, 'Brave New World', 'Chatto & Windus', 'Aldous Huxley', 'available', 4.1),
    (10, 'Crime and Punishment', 'The Russian', 'Dostoevsky', 'available', 4.5),
    (11, 'The Hobbit', 'George Allen & Unwin', 'J.R.R. Tolkien', 'available', 4.6),
    (12, 'The Lord of the Rings', 'George Allen & Unwin', 'J.R.R. Tolkien', 'available', 4.9),
    (13, 'Alice\'s Adventures ', 'Macmillan', 'Lewis Carroll', 'available', 4.7),
    (14, 'The Chronicles of Narnia', 'Geoffrey Bles', 'C.S. Lewis', 'available', 4.8),
    (15, 'The Kite Runner', 'Riverhead Books', 'Khaled Hosseini', 'available', 4.4)
] 

sql = "INSERT INTO book_details(b_id, b_name, publication, author, status, reviews) VALUES (%s, %s, %s, %s, %s, %s)"

c.executemany(sql, books)

mydb.commit()


def show():
    query= "SELECT * FROM book_details"
    c.execute(query)
    res = c.fetchall()
    print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
    for i in res:
        print(i)        
        
    
def add_book():
    a = random.randint(1,1000)
    b = str(input("Enter name of Book: "))
    c2 = str(input("Enter publication: "))
    d = str(input("Enter Author: "))    
    f = "available"
    g = float(input("Enter Reviews:"))
    query = "insert into book_details values(%s,%s,%s,%s,%s,%s)" 
    value = (a,b,c2,d,f,g)
    c.execute(query,value)
    mydb.commit()
    print("Book added to library records")
    show()           


def remove_book():
    a=str(input("Which book you want to remove:"))
    query="delete from book_details where b_name= '%s'"%(a,)
    c.execute(query)
    mydb.commit()
    print("Book successfully removed")
    show()
    

def extract_book():
    print("1. extract by name\n\
2. extract by author name\n\
3. extract by publications\n\
4. extract by availability\n\
5. extract all records")
    
    a=input("Enter your choice:")
    if a=='1':
        b=input("Enter the name of the book:")
        query="select * from book_details where b_name='%s'"%(b,)
        c.execute(query)
        w=c.fetchall()
        print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
        for i in w:
            print(i)
    elif a=='2':
        b=input("Enter the author name:")
        query="select * from book_details where author='%s'"%(b,)
        c.execute(query)
        w = c.fetchall()
        print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
        for i in w:
            print(i)
    elif a=='3':
        b=input("Enter the name of the publications:")
        query="select * from book_details where publication='%s'"%(b,)
        c.execute(query)
        w = c.fetchall()
        print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
        for i in w:
            print(i)
    elif a=='4':
        l=input("You want the record as per:\n1. available book\n2. unavailable book\n->")
        if l=='1':
            c.execute("select * from book_details where status='available'")
            k = c.fetchall()
            print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
            for i in k:
                print(i)
        else:
            c.execute("select * from book_details where status='unavailable'")
            k = c.fetchall()
            print("(Book Id, Book Name, Publications, Author, Availability Status, Reviews)")
            for i in k:
                print(i)
    
    elif a=='5':
        show()
        

def entry():
    b = str(input("Enter your name:"))
    c.execute("select c_name from customer_details")
    x = c.fetchall()
    
    if (b,) in x:
        c.execute("select * from customer_details")
        a = c.fetchall()
        for i in a:
            if i[1] == b:
                a = i[0]
        

    else:
        a = random.randint(1,1000)
        
    
    c2 = str(input("Enter your phone no:"))
    d = str(input("Enter Book name for issuing:"))
    query = "select status from book_details where b_name='%s'"%(d,)
    c.execute(query)
    o = c.fetchall()
    
    if o[0][0] == 'available':           
        query = "select b_id from book_details where b_name='%s'"%(d,)
        c.execute(query)
        x = c.fetchall()
    
        query = "update book_details set status = 'unavailable' where b_name ='%s'"%(d,)
        c.execute(query)
        mydb.commit()
    else:
        print("Book is currently unavailable")
        entry()
        
    e = str(input("Enter date of issue: "))
    f = str(input("Enter date of return: "))
    g = str(input("Do you have a membership(Y/N): "))
    if g.lower() == 'n':
        print("We offer the following packages for membership\n\
1. 1 month- Rs. 799\n\
2. 6 months- Rs. 3999\n\
3. 1 Year- Rs. 6999")
        h1 = int(input("->"))
        if h1 == 1:
            h2 = 799
        elif h1 == 2:
            h2 = 3999
        else:
            h2 = 6999    

        
    elif g.lower() == 'y':
        query = "select membership from customer_details where C_name = '%s'"%(b,)
        c.execute(query)
        H = c.fetchall()        
        if H == []:
            print("No membership found")
            print("We offer the following packages for membership\n\
1. 1 month- Rs. 799\n\
2. 6 months- Rs. 3999\n\
3. 1 Year- Rs. 6999")
        h1 = int(input("->"))
        if h1 == 1:
            h2 = 799
        elif h1 == 2:
            h2 = 3999
        else:
            h2 = 6999
       
    query = "insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s)"
    value = (a,b,c2,x[0][0],e,f,g.upper(),h2)
    c.execute(query,value)
    mydb.commit()
    print("Welcome to library") 


def extract_member_record():
    print("1. Extract all records\n\
2. Extract by name\n\
3. Extract by membership amount\n\
4. Extract by membership\n\
5. Extract by book issued")
    a = int(input("->"))
    if a == 1:
        query = "select * from customer_details"
        c.execute(query)
        res = c.fetchall()
        print("(Customer Id, Customer Name, Phone Number, Book issued(Id), Date of issue, Date of return, Is Member(Y/N), Membership Plan)")
        for i in res:
            print(i)
    elif a==2:
        p=input("Enter the name of the customer:")
        query="select * from customer_details where c_name='%s'"%(p,)
        c.execute(query)
        res=c.fetchall()
        print("(Customer Id, Customer Name, Phone Number, Book issued(Id), Date of issue, Date of return, Is Member(Y/N), Membership Plan)")
        for i in res:
            print(i)
    elif a==3:
        p=int(input("Enter the membership amount:"))
        query="select * from customer_details where membership =%s"%(p,)
        c.execute(query)
        res=c.fetchall()
        print("(Customer Id, Customer Name, Phone Number, Book issued(Id), Date of issue, Date of return, Is Member(Y/N), Membership Plan)")
        for i in res:
            print(i)
    elif a==4:
        p=input("Are you an existing member?:(Y/N)")
        query="select * from customer_details where member='%s'"%(p,)
        c.execute(query)
        res=c.fetchall()
        print("(Customer Id, Customer Name, Phone Number, Book issued(Id), Date of issue, Date of return, Is Member(Y/N), Membership Plan)")
        for i in res:
            print(i)
    else:
        p=input("Enter the name of the book issued:")
        query="select b_id from book_details where b_name='%s'"%(p,)
        c.execute(query)
        res=c.fetchall()
        query2="select * from customer_details where book_issued=%s"%(res[0][0],)
        c.execute(query2)
        res2=c.fetchall()
        print("(Customer Id, Customer Name, Phone Number, Book issued(Id), Date of issue, Date of return, Is Member(Y/N), Membership Plan)")
        for i in res2:
            print(i)              


def return_book():
    a = str(input("Enter your name: "))
    b = int(input("Enter id of Book to be returned: "))
    query = "update customer_details set Book_issued = NULL,issue_date = NULL, return_date = NULL where Book_issued= '%s'"%(b,)
    c.execute(query)
    mydb.commit()
    query = "update book_details set status = 'available' where b_id ='%s'"%(b,)
    c.execute(query)
    mydb.commit()
    
    print("Book Returned, Please visit again.")
    

def menu():
    
    print("\nChoose an option:\n\
    1. Add Book\n\
    2. Remove Book\n\
    3. Extract Book records\n\
    4. Add an Entry\n\
    5. Extract customer records\n\
    6. Return book\n\
    7. Exit")
    ch = int(input("->"))
    if ch == 1:
        add_book()
    
    elif ch == 2:
        remove_book()
        
    elif ch == 3:
        extract_book()

    elif ch == 4:
        entry()
    
    elif ch == 5:
        extract_member_record()
        
    elif ch == 6:
        return_book()

    elif ch == 7:
        sys.exit()

try:
    print("Welcome To Library")
    while True:
        menu()
except:
    print("Something went wrong... Please try again.")
    
mydb.close()  
