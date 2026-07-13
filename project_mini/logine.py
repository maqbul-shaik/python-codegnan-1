from users import user
def login(Id,password):
    if Id  in user :  
        if password == user[Id]['password']:
            print("Login successfull")
            return True
        else:
            print("Login unsuccesful")
    return False
n=int((input("enter the Id:")))
p=input("enetr the password:")
res=login(n ,p)
print(res)