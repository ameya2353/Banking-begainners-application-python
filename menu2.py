'''
Created on 08-Sep-2018

@author: AMEYA BRID
'''
import insert_cust
import sign_in
import acc_managment
from sign_in import sign_cust
x=" "
def submenu(cust_id):
    custm_id=cust_id
    print(x*70,"1. Address Change")
    print(x*70,"2. Money Deposit")
    print(x*70,"3. Money Withdrawal")
    print(x*70,"4. Print Statement")
    print(x*70,"5. Transfer Money")
    print(x*70,"6. Account Closure")
    print(x*70,"7. Customer Logout")
    ch=int(input("enter ur choice"))
    if(ch==1):
        address=input("enter address")
        s=acc_managment.manage()
        s.address(address, custm_id)
        submenu(custm_id)
        
    if(ch==2):
        amt=int(input("enter the amount"))
        s=acc_managment.manage()
        s.deposit(amt, cust_id)
        submenu(cust_id)
    if(ch==3):
        amt=int(input("enter the amount"))
        s=acc_managment.manage()
        s.withdraw(amt, cust_id)
        submenu(cust_id)
    if(ch==4):
        s=acc_managment.manage()
        s.prints(cust_id)
        submenu(cust_id)
    if(ch==5):
        amt=int(input("enter the amount"))
        trans_d=input("enter the CUSTOMER ID to which money is to be transfered")
        s=acc_managment.manage()
        s.transfer(amt, cust_id,trans_d)
        submenu(cust_id)
        
    if(ch==6):
        print("YOU WOULD BE REDIRECTED TO THE MAIN MENU DIRECTLY")
        d=input("DO Y WANT TO CLOSE YOUR ACCCOUNT Y/N?")
        if(d=='Y' or d=='y'):
            s=acc_managment.manage()
            s.acc_close(cust_id)
        elif(d=='n' or d=='N'):
            submenu(custm_id)
        
    if(ch==7):
        signin()
def menu():
    print(x*80,"MENU")
    print(x*70,"1. SIGN UP (NEW CUSTOMER)")
    print(x*70,"2. SIGN IN (EXISTING CUSTOMER)")
    print(x*70,"3. ADMIN SIGN IN")
    print(x*70,"4. QUIT")
    q=int(input("enter ur choice: "))
    return q

def signup():
    print("1.signup")
    print("2. back")
    ch=int(input("enter choice"))
    if(ch==1):
        name=input("Enter name")
        address=input("Enter Address")
        cust_id=input("Enter ID")
        password=input("Set a password")
        try:
            insert_cust.InsertCust().InsertCust(name,address,cust_id,password)
        except Exception as e:
            print("something went wrong")
            signup()
        else:
            loop()
    if(ch==2):
        loop()

def signin():
    print("1.signin")
    print("2.Main Menu")
    ch=int(input("enter choice"))
    if(ch==1):
        cust_id=input("enter customer ID")
        password=input("Enter password")
        p=sign_in.sign_cust().sign_in(cust_id, password)
        if(p==True):
            submenu(cust_id)
    if(ch==2):
        loop()
        

def adm_sign_in():
    print("1.admin sign in")
    print("2.back")
    ch=int(input("enter choice"))
    if(ch==1):
        print("admin sign in")
    if(ch==2):
        loop()


def loop():
    q=menu()
    if(q==1):
        signup()
    if(q==2):
        signin()
    if(q==3):
        adm_sign_in()
    if(q==4):
        exit()
loop(