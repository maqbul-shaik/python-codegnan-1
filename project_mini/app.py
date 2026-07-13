from logine  import res
from users import user
from viewstudent import view
from delete import delete

while res:
    print("Student Mangement System")
    print(" 1.Add student\n 2.View student\n 3.Delete student\n 4.Exit")
    choice=int(input("enter your choice :"))
    if choice == 1:
        stu=input("enter the new student id :")
        v=input("enter new student password:")
        user[stu] = {
            "password": v
        }
        print(user)
    elif choice == 2:
        n=int(input("enter the student Id: "))
        view(student=n)
    elif choice ==3:
        Id = int(input("Enter student id to Delete : "))
        print(delete(Id = Id))
    elif choice ==4:
        exit()
