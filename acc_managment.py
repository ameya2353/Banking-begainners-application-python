'''
Created on 08-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle

class manage:
    def address(self,adress,cust_id):
        self.adress=adress
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""UPDATE Bankacc SET cust_addr=:1 WHERE cust_id=:2 """,(self.adress,self.cust_id))
        con.commit()
        con.close()
    
    def acc_close(self,cust_id):
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""DELETE FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.cust_id})
        con.commit()
        con.close()
    def deposit(self,amt,cust_id):
        self.amt=amt
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT bal FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=list(map(int,b))
        curr_bal=c[0]+self.amt
        cur.execute("""UPDATE Bankacc SET bal=:1 WHERE cust_id=:2 """,(curr_bal,self.cust_id))
        con.commit()
        con.close()
        
    def withdraw(self,amt,cust_id):
        self.amt=amt
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT bal FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=list(map(int,b))
        curr_bal=c[0]-self.amt
        cur.execute("""UPDATE Bankacc SET bal=:1 WHERE cust_id=:2 """,(curr_bal,self.cust_id))
        con.commit()
        con.close()
        
    def transfer(self,amt,cust_id,trans_id):
        self.amt=amt
        self.cust_id=cust_id
        self.trans_id=trans_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT bal FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=list(map(int,b))
        curr_bal=c[0]-self.amt
        cur.execute("""UPDATE Bankacc SET bal=:1 WHERE cust_id=:2 """,(curr_bal,self.cust_id))
        cur.execute("""SELECT bal FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.trans_id})
        b=cur.fetchone()
        c=list(map(int,b))
        curr_bal=c[0]+self.amt
        cur.execute("""UPDATE Bankacc SET bal=:1 WHERE cust_id=:2 """,(curr_bal,self.trans_id))
        con.commit()
        con.close()
     
    def prints(self,cust_id):
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Bankacc WHERE cust_id=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        print("customer_ID= ",b[0])
        print("customer name= ",b[1])
        print("address= ",b[2])
        print("BALANCE= ",b[3])
        con.commit()
        con.close()     
    
# #         
# s=manage()
# s.prints('ameya2353')      