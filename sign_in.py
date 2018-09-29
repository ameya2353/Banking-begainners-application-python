'''
Created on 08-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
class sign_cust:
    def sign_in(self,cust_id,password):
        self.cust_id=cust_id
        self.passw=password
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Bankacc WHERE cust_id=:1 and password=:2""",(self.cust_id,self.passw))
        if(cur.fetchall()):
            return True
        else:
            return False
        con.commit()
        con.close()
# if(cur.fetchall()):
#         
#         else:
#             return False
#         
# s=sign_in()
# q=s.sign_in('ameya2353','beastmode')
# print(q)