
#PYTHON MODULE: MenuDoctor
import mysql.connector


#Insert Record
def insertDoctor():
        
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='hospital')
    Cursor=cnx.cursor()
    Dno=input("Enter Doctor Code:")
    Dname=input("Enter Doctor Name:")
    sp_list=input("Doctor's Spacialist")
    MOB=input("Enter Doctor Mobile Number:")
    ADR=input("Enter doctor's address")
        
    Qry=("INSERT INTO Doctor VALUES(%s,%s,%s,%s,%s)")
    date=(Dno,Dname,sp_list,MOB,ADR)
    Cursor.execute(Qry,data)
    Cursor.commit()
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    cnx.close()
    print("Record Inserted .........")

#Display

def display():
    cnx=mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='hospital')
    Cursor = cnx.cursor()
    query=("SELECT * FROM Doctor")
    Cursor.execute(query)
    for (Dno,Dname,sp_list,MOB,ADR)in Cursor:
        print("====================================================================================")
        print("Doctor Code:",Dno)
        print("Doctor Name:",Dname)
        print("Doctor's Specialist :",sp_list)
        print("Mobile Number Of Doctor:",MOB)
        print("Address:",ADR)
            
            
        print("====================================================================================")
        Cursor.close()
        cnx.close()
        print("you have done it!!!!!!!!")
    

   

#Delete Record
def DeleteDoctor():
        
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='hospital')
    Cursor=cnx.cursor()
    Dno=input("Enter Doctor Code to be Deleted from the hospital:")
    Qry=("""DELETE FROM Doctor WHERE Dno=%s""")
    del_rec=(Dno,)
    Cursor.execute(Qry,del_rec)
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    cnx.close()
    print("Cursor.rowcount,'Record(s) Deleted Successfully.........")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#Search Record
def SearchDoctor():
        
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost',database='hospital')
    Cursor=cnx.cursor()
    Dno=input("Enter Doctor Name to be Searched from the hospital")
    query= ("SELECT * FROM Doctor WHERE Dno=%s")
    rec_sech=(Dno,)
    Cursor.execute(query,rec_sech)
    Rec_count=0
    for (Dno,Dname,sp_list,MOB,ADR)in Cursor:
        print("====================================================================================")
        print("Doctor Code:",Dno)
        print("Doctor Name:",Dname)
        print("Doctor's spacialist",sp_list)
            
        print("Mobile no. of Doctor",MOB)
        print("ADDRESS",ADR)
            
        print("====================================================================================")
        if Rec_count%2==0:
            input("Press any key to continue")
            print(Rec_count, "Record(s) found")

        Cursor.close()
        print("record searched.........")


#Update Record
def UpdateDoctor():
    cnx=mysql.connector.connect(host='localhost',user='root',password='Bharat@123',database='hospiatal')
    Cursor=cnx.cursor()
    print("Enter new data")
    Dno=input("ENTER Doctor code")
    Dname=input("Enter doctor Dname")
    sp_list=input("Doctor's spacialist")
    MOB= input("Mobile no. of Doctor")
    ADR=input("enter Address")
    Qry=("UPDATE DoctorRecord SET    Dno=%s,Dname=%s,sp_list=%s,MOB=%s,ADR=%s,WHERE Dno=%s") 
    data=(Pno,Pname,gender,age,disease,PhNo)
    Cursor.execute(Qry,data)
    cnx.commit()
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    cnx.close()
    print(Cursor.rowcount,"Record(s) Update Successfully.........")

