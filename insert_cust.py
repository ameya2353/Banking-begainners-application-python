'''
Created on 08-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
class  InsertCust:
    
    def InsertCust(self,name,address,cust_Id,password):
        bal=0
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""INSERT INTO Bankacc VALUES(:1,:2,:3,:4,:5) """,(cust_Id,name,address,bal,password))
        con.commit()
        con.close()
    


