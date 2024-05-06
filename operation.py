#  Importing the required modules/libraries
import datetime

# Function to perform the operations of renting and returning the land
def choice_():
    print("-------------------------------------------------------------------------------------------------")
    print("******************************Techno Property Nepal *********************************************")
    print("-------------------------------------------------------------------------------------------------")
    print("Provided facilities::")
    print("1. Rent lands")
    print("2. Return rented lands")
    print("3. Exit")

# Function to print the heading
def heading():
    print("-------------------------------------------------------------------------------------------------")
    print("******************************Techno Property Nepal *********************************************")
    print("-------------------------------------------------------------------------------------------------")
 
# Function to validate the name i.e check if the name contains only alphabets
def validate_name(name):
    return all(char.isalpha() or char.isspace() for char in name)

check = True # Declaring a variable to check the condition
# Function to rent the land
def rent():
    d = {}
    file = open('land.txt', 'r') # Opening the file to read the data
    data = file.readlines()  # Reading the data from the file
    for line in data: # Looping through the data
        col = line.split() # Splitting the data
        key = col[0] # Storing the land ID in key
        value = {   # Storing the location, direction, anna, price and status in value
            'Location': col[1],
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:]) # Joining the status
        }
        d[key] = value # Storing the value in the directory
    try:
        # Check if the land is available or not
        land_id = input("Enter the land ID you want to rent::")
        if land_id in d.keys(): # Checking if the land ID is in the directory
            if d[land_id]['Status'] == 'Available': # Checking if the land is available
                d[land_id]['Status'] = 'Not_Available' # Setting the status of land as not available in directory
                while check: # Looping through the condition
                    name = input("Enter your name::") # Taking name as input to print it in bill
                    if validate_name(name): # Checking if the name is valid
                        break
                    else:
                        print("Invalid input. Please enter a valid name containing only alphabets.")

                while check: # Looping through the condition
                    phone = int(input("Enter your phone number::\t+977 ")) # Taking phone as input to print it in bill
                    if(len(str(phone)) != 10):  # Checking if the phone number is valid
                        print("Invalid phone number")
                    else:
                        break

                while check: # Looping through the condition
                    month = int(input("Enter the number of months you want to rent the land::" )) # Taking the number of months as input
                    if month < 1: # Checking if the number of months is valid
                        print("Invalid input")
                    else:
                        break
                location = d[land_id]['Location'] # Storing the location of land
                direction = d[land_id]['Direction'] # Storing the direction of land
                anna = d[land_id]['Anna'] # Storing the anna of land

                #Calculation of total price
                total_price = int(d[land_id]['Price']) * month # Calculating the total price for renting the land
                print("Total price for renting the land for", month, "months is Rs.", total_price) # Printing the total price
                print("Land rented successfully") 
                return land_id, name, phone, month, total_price, location, direction, anna # Returning the values to main function
            else:
                print("Land is already rented") # Printing if the land is already rented
        else:
            print("Land ID not found")
    except ValueError:
        print("Invalid input") # Printing if the input is invalid
    file.close()


# Function to return the rented land
def return_land():
    d = {} # Declaring the directory
    file = open('land.txt', 'r') # Opening the file to read the data
    data = file.readlines() # Reading the data from the file
    for line in data: # Looping through the data
        col = line.split() # Splitting the data
        key = col[0] # Storing the land ID in key
        value = { # Storing the location, direction, anna, price and status in value
            'Location': col[1],
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value # Storing the value in the directory
    try:
        # Check if the land is available or not
        while check: # Looping through the condition
            land_id = input("Enter the land ID you want to return::")
       
            if land_id in d.keys(): # Checking if the land ID is in the directory
                before = d[land_id]['Status'] # Storing the status of land before returning
                if d[land_id]['Status'] == 'Not_Available': # Checking if the land is rented
                    d[land_id]['Status'] = 'Available' #Setting the status af land as available in directory
                    break
            else:
                print("Land ID not found") # Printing if the land ID is not found
                print("Please enter the correct land ID") # Printing the message to enter the correct land ID
        
    except:
        print("Invalid input") # Printing if the input is invalid
    file.close()
    return land_id, before # Returning the values to main function

# Function to find the fine for rent of land
def bill_fine(land_id): 
    # Asking the user to enter the number of months the land is rented
    while check:  # Looping through the condition
        month = int(input("Enter the number of months you rented the land::" ))
        if month < 1: # Checking if the number of months is valid
            print("Invalid input")
        else:
            break

    # Asking the user to enter the number of months the land is returned
    while check: # Looping through the condition
        time = int(input("Enter the number of months you took to return the land::"))
        if month < 1: # Checking if the number of months is valid
            print("Invalid input")
        else:
            break
    
    d = {} # Declaring the directory
    file = open('land.txt', 'r')  # Opening the file to read the data
    data = file.readlines() # Reading the data from the file
    for line in data: # Looping through the data
        col = line.split()
        key = col[0] # Storing the land ID in key
        value = {
            'Location': col[1], # Storing the location in value
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value # Storing the value in the directory
    total_price = int(d[land_id]['Price']) * month # Calculating the total price for renting the land

    # Checking if the land is returned at the correct time
    if (time == month or time < month):
        fine = 0 # Setting the fine as 0
        print("Total price for renting the land for", month, "months is Rs.", total_price) # Printing the total price
        print("Land returned successfully")
        
    # Checking if the land is returned late
    elif time > month: # Checking if the land is returned late
        fine = (time - month) * int(d[land_id]['Price']) # Calculating the fine for returning the land late
    return fine,month # Returning the fine and month to main function

# Function to print the bill for rent of land
def bill(land_id ,location , direction, anna, name, phone, month, total_price): 
    heading() # Printing the heading
    print("Bill") # Printing the bill
    print("-------------------------------------------------------------------------------------------------") 

    unique = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Storing the unique value
    date = datetime.date.today().strftime("%Y-%m-%d") # Storing the date
    time = datetime.datetime.now().time().strftime("%H:%M:%S") # Storing the time

    # Printing the details in the bill
    print("Date::", date,'\t\t\t' "Time::", time)
    print("Land ID::", land_id, '\t\t\t' "Direction::", direction)  
    print("Location::", location, '\t\t\t' "Anna::", anna) 
    print("Name::", name)
    print("Phone::", phone)
    print("Months::", month)
    print("Total price::", total_price)
    print("Bill printed successfully")
    print("-------------------------------------------------------------------------------------------------")
    
    # Writing the bill in a file
    file = open('bill_'+ str(unique)+'.txt', 'w') # Opening the file to write the data
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("******************************Techno Property Nepal *********************************************\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Bill\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Date:: " + date + '\t\t\t' "Time:: " + time + '\n')
    file.write("Land ID:: " + land_id  + '\t\t\t' "Direction:: " + direction + '\n')
    file.write("Location:: " + location + '\t\t\t' "Anna:: " + anna + '\n')
    file.write("Name:: " + name + '\n')
    file.write("Phone:: " + str(phone) + '\n')
    file.write("Months:: " + str(month) + '\n')
    file.write("Total price:: " + str(total_price) + '\n')
    file.write("Bill printed successfully\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.close()

# Function to print bill for returning the land
def bill_return(fine,month,land_id):
    d={}    #Declaring directory    
    file = open('land.txt','r')#Opening file to read the data
    data = file.readlines() #Reading the data from the file
    for line in data:   #Looping through the data
        col = line.split()
        key = col[0]
        value = {
            'Location': col[1],
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value
    
    while check:
        name = input("Enter your name::") # Taking name as input to print it in bill
        if validate_name(name): # Checking if the name is valid
            break
        else:
            print("Invalid input. Please enter a valid name containing only alphabets.")
    while check:
        phone = int(input("Enter your phone number::\t+977 ")) # Taking phone as input to print it in bill
        if(len(str(phone)) != 10): # Checking if the phone number is valid
            print("Invalid phone number")
        else:
            break
    location = d[land_id]['Location'] # Storing the location of land
    direction = d[land_id]['Direction'] # Storing the direction of land
    anna = d[land_id]['Anna'] # Storing the anna of land
    total_price = (int(d[land_id]['Price']) * month) + fine # Calculating the total price for renting the land

    #  Printing the bill for returning the land
    heading()
    print("Bill")
    print("-------------------------------------------------------------------------------------------------")

    # Printing the details in the bill
    unique = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.date.today().strftime("%Y-%m-%d")
    time = datetime.datetime.now().time().strftime("%H:%M:%S")

    # Printing the details in the bill
    print("Date::", date,'\t\t\t' "Time::", time)
    print("Land ID::", land_id, '\t\t\t' "Direction::", direction)
    print("Location::", location, '\t\t\t' "Anna::", anna)
    print("Name::", name)
    print("Phone::", phone)
    print("Months::", month)
    print("Total price::", total_price)
    print("Land returned successfully")
    print("-------------------------------------------------------------------------------------------------")
    
    # Writing the bill in a file
    file = open('bill_'+ str(unique)+'.txt', 'w') # Opening the file to write the data

    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("******************************Techno Property Nepal *********************************************\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Bill\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Date:: " + date + '\t\t\t' "Time:: " + time + '\n')
    file.write("Land ID:: " + land_id + '\t\t\t' "Direction:: " + direction + '\n')
    file.write("Location:: " + location + '\t\t\t' "Anna:: " + anna + '\n')
    file.write("Name:: " + name + '\n')
    file.write("Phone:: " + str(phone) + '\n')
    file.write("Months:: " + str(month) + '\n')
    file.write("Total price:: " + str(total_price) + '\n')
    file.write("Land returned successfully\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.close()
