'''
Created on 08-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
cur=con.cursor()
# cur.execute("""CREATE TABLE Bankacc(
#                   cust_id VARCHAR2(10) PRIMARY KEY,
#                   cust_name CHAR(20),
#                   cust_addr VARCHAR2(20),
#                   bal NUMBER         
#                             ) """)
cur.execute("ALTER TABLE Bankacc ")
# cur.execute("""SELECT * FROM Bankacc""")
# print(cur.fetchall())
con.commit()
con.close()