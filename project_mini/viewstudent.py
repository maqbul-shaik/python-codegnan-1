from users import user
def view(student:int):
    if student in user:
        print( "student details")
        print(f"Branch : {user[student]['branch']} student percentage is : {user[student]['percentage']}")
    else:
        print("wrong student id")

