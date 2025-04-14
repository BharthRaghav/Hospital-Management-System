import MenuHospital
while True:
    print("\t\t\t Hospital Management System\n")
    print("====================================================================")
    print("1.Patient Management")
    print("2.Doctor Management ")
    print("3.Exit")
    choice=int(input("enter Choice between 1 to 3---->"))
    if choice==1:
        MenuHospital.MenuPatient()
    elif choice==2:
        MenuHospital.MenuDoctor()
    elif choice==3:
          break
    else:
        print("wrong choice....enter your choice again")
        x=input("enter any key to continue")

