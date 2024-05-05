# imporing all the necessary modules
from read import read
from operation import heading,choice_,rent,return_land,bill,bill_fine,bill_return
from write import update_status,update_returnStatus




#Declaring variable to check if the user wants to continue the program
program_run = True
while(program_run == True):
    try:
        # Checking if the user choosed frist option
        choice_()
        choice = int(input('Enter your choice::'))
        
        if(choice == 1):
            heading()
            read()
            check_empty= rent()
            if not check_empty:
                continue
            land_id, name, phone, month, total_price, location, direction, anna = check_empty
           
            update_status(land_id)
            bill(land_id ,location , direction, anna, name, phone, month, total_price)
            a = input(("Do you wish to continue using our system:: y/n\t")).lower()
            if(a =='y'):
                continue
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
            if stat == 'Available' :
                print("Land is already available")
            else:
                fine,month_ = bill_fine(land_id) # Calling the function to calculate the fine
                update_returnStatus(land_id)
                bill_return(fine,month_,land_id)
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
    except:
        print("Invalid input")
        print('\n')
