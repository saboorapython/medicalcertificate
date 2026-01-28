

# Scenario 1

#let me know, if i am allowed to sit in exam!

name=input("Your Name:")
tclss=int(input("Enter a number of total classes:"))
clss=int(input("Enter a number of attandance / classes attanded: (in No(s)):"))

per=(clss/tclss)*100

if per>=75:
    print("You're Allowed to sit in exam! No Medical")
elif per>=20 and per<75:
    print(f"Dear {name} Your Percentage is below 75%")
    med_c=int(input("Do you have Medical Certificate?: \Press 1. for Yes \nPress 2. For No \n:"))
    if med_c==1:
        print("Your medical certificate is processed for verification:")
        ver=int(input("Let me know is it signed and stampped ? : \nPress 1. for Yes \nPress 2. for No:"))
        if ver==1:
            print(f"Dear {name}, Despit your Attandance is low, but Your Medical Certificate is verified and your're Allowed to sit in exam!")
        elif ver==2:
            print(f"Dear {name}, Your Attandance is low and Your Medical Certificate is Not verified and your're Not Allowed to sit in exam!")
        else:
            print("Invalid input")  
    else:
        print("You're Not Allowed to sit in exam!")
else:
    print("Attandance Percentage is very low! you're Not Allowed!")
