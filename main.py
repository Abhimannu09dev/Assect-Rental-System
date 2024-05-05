# imporing all the necessary modules
from read import read
from operation import heading,choice_,rent,return_land,bill,bill_fine
from write import update_status,update_returnStatus




#Declaring variable to check if the user wants to continue the program
program_run = True
while(program_run == True):
    try:
        # Checking if the user choosed frist option
        choice_()
        choice = int(input('Enter your choice::'))
        
        if(choice == 1):
            read()
            check_empty= rent()
            if not check_empty:
                print("Land not available")
                continue
            land_id, name, phone, month, total_price = check_empty
           
            update_status(land_id)
            bill(land_id, name, phone, month, total_price)
            a = input(("Do you wish to continue using our system:: y/n\t")).lower()
            if(a =='y'):
                choice_()
            elif(a =='n'):
                print("Thank you for using our system.")
                print("Please visit again")
                program_run=False
                break
            else:
                print("Invalid input")

        elif (choice == 2):
            read()
            land_id,stat = return_land()
            if stat == 'Available':
                print("Land is already available")
            else:
                update_returnStatus(land_id)
                month = int(input("Enter the number of months you rent the land::"))
                bill_fine(month, land_id) # Calling the function to calculate the fine

            a = input(("Do you wish to continue using our system:: y/n\t")).lower()
            if(a == 'y'):
                choice_()
            elif(a == 'n'):
                print("Thank you for using our system.")
                print("Please visit again")
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
        print('\n')
