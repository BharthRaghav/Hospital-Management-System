#PYTHON MODULE: MenuHospital
import Patient
import Doctor

k=1
a=2
def MenuPatient():
    global k
    while k==1:
        print("\t\t\t Patient Records Management\n")
        print("===================================================================================")
        print("1.Add Patient Record")
        print("2.Display Patient Records")
        print("3.Search Patient Record")
        print("4.Delete patient Record")
        print("5.Update patient Record")
        print("6.Return to Main Manu")
        print("====================================================================================")
        choice=int(input("enter choice between 1 to 6----->"))
        if choice==1:
            Patient.insertData()
        elif choice==2:
            Patient.display()
        elif choice==3:
            Patient.SearchPatientRec()
        elif choice==4:
            Patient.DeletePatient()
        elif choice==5:
            Patient.UpdatePatient()
        elif choice==6:
            return
        else:
            print("wrong choice......enter your choice again")
            k=1
            
def MenuDoctor():
    
    global a
    while a==2:
        
        print("\t\t\t Doctor Records Management\n")
        print("===================================================================================")
        print("1.Add Doctor Record")
        print("2.Display Doctor Records")
        print("3.Search Doctor Record")
        print("4.Delete Doctor Record")
        print("5.Update Doctor Record")
        print("6.Return to Main Manu")
        print("====================================================================================")
        choice=int(input("enter choice between 1 to 6----->"))
        if choice==1:
            Doctor.insertData()
        elif choice==2:
            Doctor.display()
        elif choice==3:
            Doctor.SearchDoctorRec()
        elif choice==4:
            Doctor.DeleteDoctor()
        elif choice==5:
            Doctor.UpdateDoctor()
        elif choice==6:
            return
        else:
            print("wrong choice......enter your choice again")
           
