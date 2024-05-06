# imporing all the necessary modules
from read import read
from operation import heading,choice_,rent,return_land,bill,bill_fine,bill_return
from write import update_status,update_returnStatus


#Declaring variable to check if the user wants to continue the program
program_run = True 
while(program_run == True): # Running the program until the user wants to exit
    try: # Exception handling
        choice_() # Function to display the choices
        choice = int(input('Enter your choice::')) # Taking the choice from the user
        
        if(choice == 1): # If the user wants to rent the land
            heading() # Function to display the heading
            read() # Function to display the available lands
            check_empty= rent() # Function to rent the land
            if not check_empty: # If the user has not entered any input
                continue
            land_id, name, phone, month, total_price, location, direction, anna = check_empty # Assigning the values to the variables
           
            update_status(land_id) # Updating the status of the land
            bill(land_id ,location , direction, anna, name, phone, month, total_price) # Generating the bill
            a = input(("Do you wish to continue using our system:: y/n\t")).lower() # Asking the user if they want to continue
            if(a =='y'): # If the user wants to continue
                continue
            elif(a =='n'): # If the user wants to exit
                print("Thank you for using our system.")
                print("Please visit again")
                program_run=False # Setting the variable to False to exit the program
                break
            else: # If the user enters invalid input
                print("Invalid input")

        elif (choice == 2): # If the user wants to return the land
            heading() # Function to display the heading
            read() # Function to display the available lands
            land_id,stat = return_land() # Function to return the land
            if stat == 'Available' : # If the land is already available
                print("Land is already available")
            else:
                fine,month_ = bill_fine(land_id) # Calling the function to calculate the fine
                update_returnStatus(land_id)     # Updating the status of the land
                bill_return(fine,month_,land_id) # Generating the bill
            a = input(("Do you wish to continue using our system:: y/n\t")).lower()
            if(a == 'y'): # If the user wants to continue
                choice_() # Function to display the choices
            elif(a == 'n'): # If the user wants to exit
                print("Thank you for using our system.")
                print("Please visit again")
                program_run=False # Setting the variable to False to exit the program
                break
            else:
                print("Invalid input")

        elif (choice == 3): # If the user wants to exit
            print("Thank you for using our system.")
            print("Please visit again")
            program_run =False # Setting the variable to False to exit the program
        else:
            print("Invalid input")
    except: # If the user enters invalid input
        print("Invalid input")
        print('\n')
