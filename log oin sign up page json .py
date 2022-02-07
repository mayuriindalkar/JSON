print("***Welcome to log in sign up page****")

user=input("what you want sign up or login account? ")
if user=="sign":
    name=input("enter the name ")
    last_name=input("enter the last_name ")
    password=input("enter your password ")
    confirm_password=input("enter your password ")
    if "@" in password or "#" in password:
        if password==confirm_password:
            print("**Account has created succesfull**,hureee")

            a=open("login.txt","w")
            new_file=a.write("name :- ")
            new_file=a.write(name)
            new_file=a.write("/n")

            new_file=a.write("last_name :-")
            new_file=a.write(last_name)
            new_file=a.write("/n")

            new_file=a.write("password :-")
            new_file=a.write(password)
            new_file=a.write("/n")
            a.close()
        else:
            print("your password is wrong ")
    else:
        print("in password no special chractors ")
elif user=="login":
    name1=input("enter your name : ")
    file=open("login.txt","r")
   
    new_file1=file.read()
    if name1 in new_file1:
        password1=input("enter your password :")
        if password1 in new_file1:
            print("****login succesfull****")
        else:
            print("password is wrong ")
    else:
        print("user name is wrong")