import random
import string
import mysql.connector as connector


class Books:
    def __generaterandomid(self):
        alpha = random.choices(string.ascii_letters, k=3)
        digit = random.choices(string.digits, k=3)
        symbol = random.choices("@-_#$&*", k=2)
        seq = alpha + digit + symbol
        random.shuffle(seq)
        return "".join(seq)

    def __init__(self):
        try:
            self.__conn = connector.connect(host="localhost", port="3306", user="root",
                                            password="master", database="books", auth_plugin="mysql_native_password")
            self.__cursor = self.__conn.cursor()
            print("CONNECTION ID: ", self.__conn.connection_id)
        except Exception as err:
            print("CONNECTION ERROR:", err)

    def ReadAll(self):
        try:
            sql = '''select * from book;'''
            self.__cursor.execute(sql)
            result = self.__cursor.fetchall()
            print(result)
        except Exception as err:
            self.__conn.close()
            print("ERROR WHILE READING ALL BOOKS:", err)

    def CreateBook(self):
        try:
            id = self.__generaterandomid()
            name = input("BOOK NAME: ")
            author = input("AUTHOR NAME: ")
            pages = int(input("NUMBER OF PAGES: "))
            price = float(input("BOOK PRICE: "))
            sql = f'''insert into book values('{id}', '{name}', '{author}', {pages}, {price});'''
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("BOOK ADDED IN THE LIBRARY.")
        except Exception as err:
            self.__conn.close()
            print("ERROR WHILE CREATING BOOK:", err)

    def ReadBook(self):
        try:
            print("1. SEARCH BY BOOK ID: ")
            print("2. SEARCH BY BOOK NAME: ")
            print("3. SEARCH BY AUTHOR NAME: ")
            op = int(input('Enter Choice: '))
            if op == 1:
                id = input("Enter ID: ")
                sql = f'''select * from book where id='{id}';'''
                self.__cursor.execute(sql)
                result = self.__cursor.fetchone()
                print(result)
            elif op == 2:
                name = input("Enter Book Name: ")
                sql = f'''select * from book where name='{name}';'''
                self.__cursor.execute(sql)
                result = self.__cursor.fetchone()
                print(result)
            elif op == 3:
                author = input("Enter Author Name: ")
                sql = f'''select * from book where author='{author}';'''
                self.__cursor.execute(sql)
                result = self.__cursor.fetchall()
                print(result)
            else:
                raise KeyboardInterrupt("WRONG INPUT! TRY AGAIN.")
        except Exception as err:
            self.__conn.close()
            print("ERROR WHILE READING BOOK:", err)

    def DeleteBook(self):
        try:
            id = input("Enter Id: ")
            sql = f'''delete from book where id='{id}';'''
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("BOOK REMOVED FROM THE LIBRARY.")
        except Exception as err:
            self.__conn.close()
            print("ERROR WHILE DELETING BOOK:", err)

    def UpdateBook(self):
        try:
            print("1. UPDATE BOOK NAME: ")
            print("2. UPDATE BOOK AUTHOR: ")
            print("3. UPDATE BOOK PRICE: ")
            print("4. UPDATE BOOK PAGE COUNT: ")
            op = int(input('Enter Choice: '))
            id = input("Enter Book Id: ")
            if op == 1:
                name = input("BOOK NAME: ")
                sql = f'''update book set name='{name}' where id='{id}';'''
            elif op == 2:
                author = input("AUTHOR NAME: ")
                sql = f'''update book set author='{author}' where id='{id}';'''
            elif op == 3:
                price = input("PRICE: ")
                sql = f'''update book set price={price} where id='{id}';'''
            elif op == 4:
                pages = input("NUMBER OF PAGES: ")
                sql = f'''update book set pages={pages} where id='{id}';'''
            else:
                raise KeyboardInterrupt("WRONG INPUT, TRY AGAIN.")
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("BOOK UPDATED FROM THE LIBRARY.")
        except Exception as err:
            self.__conn.close()
            print("ERROR WHILE UPDATING BOOK:", err)


book = Books()
ReadAll = book.ReadAll
# ReadAll()
CreateBook = book.CreateBook
# CreateBook()
ReadBook = book.ReadBook
# ReadBook()
DeleteBook = book.DeleteBook
# DeleteBook()
UpdateBook = book.UpdateBook
# UpdateBook()
