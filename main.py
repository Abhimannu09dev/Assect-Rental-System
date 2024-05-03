from read import read
from operation import design,choice_,rent

#Maiking the design for the company home page
choice_()

#Declaring variable to check if the user wants to continue the program
program_run = True
while(program_run == True):
    try:
        choice = int(input('Enter your choice::'))
        design()
        if(choice == 1):
            read()
            rent()
            a = input(("Do you wish to continue using our system:: y/n").lower())
            if(a=="y"):
                choice_()
                continue
            elif(a=="n"):
                program_run=False
                break
            else:
                print("Invalid input")

        elif (choice == 2):
            design()
            print("\n")
            read()
            a = input(("Do you wish to continue using our system:: y/n").lower())
            if(a=="y"):
                choice_()
                continue
            elif(a=="n"):
                program_run=False
                break
            else:
                print("Invalid input")
        elif (choice == 3):
            print("Thank you for using our system.")
            print("Please visit again")
            program_run =False
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
        continue
