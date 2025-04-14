#PYTHON MODULE: MenuPatient
import mysql.connector
# Insert
def insertData():
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Bharat@123",database="hospital")
    Cursor=cnx.cursor()
    Pno=input("Enter Patient Room no:")
    Pname=input("Enter Patient Name:")
    gender= input("Enter Patient Gender:")
    age=input("Enter Patient Age")
    disease=input("Enter Patient Disease")
    PhNo=input("Enter Patient's Phone Number")
        
    Qry=("INSERT INTO PatientRecord VALUES(%s,%s,%s,%s,%s,%s)")
    data=(Pno,Pname,gender,age,disease,PhNo)
    Cursor.execute(Qry,data)
    cnx.commit()
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    print("record Inserted.........")
    cnx.close()

#Display
def display():
    cnx=mysql.connector.connect(user='root', passwd='Bharat@123',host='localhost',database='Hospital')
    Cursor=cnx.cursor()
    query=("SELECT * FROM PatientRecord")
    Cursor.execute(query)
    for(Pno,Pname,gender,age,PhNo,disease) in Cursor:
        print("====================================================================================")
        print("Patient Room no:",Pno)
        print("Patient name:",Pname)
        print("Gender:",gender)
        print("Age:",age)
        print("phone no:",PhNo)
        print("Patient disease:",disease)
        print("====================================================================================")
        Cursor.close()
        cnx.close()
        print("you have done it!!!!!!!!")
   



#Delete
def DeletePatient():
        
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='Hospital')
    Cursor = cnx.cursor()
    Pno=input("Enter Patient Room no of the Patient to be deleated from the Hospital :")
    Qry= ("""DELETE FROM PatientRecord WHERE Pno = %s""")
    del_rec=(Pno,)
    Cursor.execute(Qry,del_rec)
    cnx.commit()
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    print("record deleted.........")
    cnx.close()

#Search record
def SearchPatientRec():
        
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='Hospital')
    Cursor = cnx.cursor()
    Pno=input("Enter Patient Room no of the Patient to be Searched from the Hospital :")
    query = ("SELECT * FROM PatientRecord WHERE Pno = %s")
    rec_srch=(Pno,)
    Cursor.execute(query,rec_srch)
    Rec_count=0
    for(Pno,Pname,gender,age,PhNo,disease) in Cursor:
        Rec_count=+1
        print("====================================================================================")
        print("Patient Room no:",Pno)
        print("Patient name:",Pname)
        print("Gender:",gender)
        print("Age:",age)
        print("phone no:",PhNo)
        print("Patient disease:",disease)
          
        print("====================================================================================")
        if Rec_count%2==0:
            input("press any key to continue")
            print(Rec_count,"RECORD(s) found")
        Cursor.close()
        print("record searched.........")
#Update
def UpdatePatient():
      
    cnx = mysql.connector.connect(user='root',passwd='Bharat@123',host='localhost', database='Hospital')
    Cursor = cnx.cursor()
   
    print("Enter new Data")
    Pno=input("Enter Patient Room no:")
    Pname=input("Enter Patient Name:")
    gender= input("Enter Patient Gender:")
    age=input("Enter Patient Age")
    disease=input("Enter Patient Disease")
    PhNo=input("Enter Patient's Phone Number")
        
    Qry=("UPDATE PatientRecord SET Pname=%s,gender=%s,age=%s,disease=%s,PhNo=%s WHERE Pno=%s")
    data=(Pno,Pname,gender,age,disease,PhNo)
    Cursor.execute(Qry,data)
    cnx.commit()
#make sure data is committed to the database cnx.commit()
    Cursor.close()
    cnx.close()
    print(Cursor.rowcount,"Record(s) Update Successfully.........")


