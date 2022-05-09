# import pyodbc
#
# connection_string = ("Driver={SQL Server Native Client 11.0};"
#                      "Server=LAPTOP-AQVJMLNP;"
#                      "Database=candycrush;"
#                      "UID=sa;"
#                      "PWD=sa;")
# connection = pyodbc.connect(connection_string)
# connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
# connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
# connection.setencoding(encoding='utf-8')
# cursor = connection.cursor()
# query = "SELECT * FROM tblUser ORDER BY -scores"
# datas = cursor.execute(query)
# for data in datas:
#     if data:
#         print(data)

import sqlite3


# con = sqlite3.connect('example.db')
# cur = con.cursor()
# cur.execute('''CREATE TABLE tblUser
#                 (username, scores)''')
# cur.execute("INSERT INTO tblUser VALUES('Truong Nhu Dat',12313)")
# cur.execute("INSERT INTO tblUser VALUES('Truong Nhu Dat 1',23)")
# cur.execute("INSERT INTO tblUser VALUES('Truong Nhu Dat 2',1231)")
# cur.execute("INSERT INTO tblUser VALUES('Truong Nhu Dat 3',231231)")
# con.commit()
# for row in cur.execute("SELECT * FROM tblUser ORDER BY -scores"):
#     print(row)

class Database:
    def __init__(self):
        self.con = sqlite3.connect('database/example.db')
        self.cur = self.con.cursor()

    def insert(self, name, scores):
        query = f"INSERT INTO tblUser VALUES({name},{scores})"
        self.cur.execute(query)
        self.con.commit()

    def update(self, name, value):
        query = f"UPDATE tblUser SET scores = {value} WHERE name = {name}"
        self.cur.execute(query)
        self.con.commit()

    def select(self):
        query = "SELECT * FROM tblUser ORDER BY -scores"
        return self.cur.execute(query)


# db = Database()
# for row in db.select():
#     print(row[0],row[1])
