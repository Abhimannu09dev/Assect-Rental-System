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
 
# Function to rent the land
def rent():
    d = {}
    file = open('land.txt', 'r')
    data = file.readlines()
    for line in data:
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
    try:
        # Check if the land is available or not
        land_id = input("Enter the land ID you want to rent::")
        if land_id in d.keys():
            if d[land_id]['Status'] == 'Available':
                d[land_id]['Status'] = 'Not_Available' # Setting the status of land as not available in directory
                name = input("Enter your name::") # Taking name as input to print it in bill
                phone = int(input("Enter your phone number::")) # Taking phone as input to print it in bill
                month = int(input("Enter the number of months you want to rent the land::" ))

                #Calculation of total price
                total_price = int(d[land_id]['Price']) * month
                print("Total price for renting the land for", month, "months is Rs.", total_price)
                print("Land rented successfully")
                return land_id,name, phone, month, total_price
        else:
            print("Land ID not found")
    except ValueError:
        print("Invalid input")
    file.close()

# Function to return the rented land
def return_land():
    d = {}
    file = open('land.txt', 'r')
    data = file.readlines()
    for line in data:
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
    try:
        # Check if the land is available or not
        land_id = input("Enter the land ID you want to return::")
        before = d[land_id]['Status']
        if land_id in d.keys():
            if d[land_id]['Status'] == 'Not_Available':
                d[land_id]['Status'] = 'Available' #Setting the status af land as available in directory
        else:
            print("Land ID not found")
    except ValueError:
        print("Invalid input")
    file.close()
    return land_id, before

# Function to find the fine for rent of land
def bill_fine(month, land_id):
    

    # Asking the user to enter the number of months the land is rented
    time = int(input("Enter the number of months you took to return the land::"))

    d = {} # Declaring the directory
    file = open('land.txt', 'r')  # Opening the file to read the data
    data = file.readlines() # Reading the data from the file
    for line in data:
        col = line.split()
        key = col[0] # Storing the land ID in key
        value = {
            'Location': col[1], # Storing the location in value
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value
    total_price = int(d[land_id]['Price']) * month # Calculating the total price for renting the land

    # Checking if the land is returned at the correct time
    if (time == month or time < month):
        print("Total price for renting the land for", month, "months is Rs.", total_price)
        print("Land returned successfully")
        
    # Checking if the land is returned late
    elif time > month:
        fine = (time - month) * int(d[land_id]['Price']) # Calculating the fine for returning the land late
        print("Total price for renting the land for", month, "months is Rs.", total_price)
        print("Fine for returning the land late is Rs.", fine)
        print("Total price for renting the land for", time, "months is Rs.", total_price + fine)

# Function to print the bill for rent of land
def bill(land_id , name, phone, month, total_price):
    heading()
    print("Bill")
    print("-------------------------------------------------------------------------------------------------")
    date = datetime.date.today()
    print("Date::", date)
    print("Land ID::", land_id)
    print("Name::", name)
    print("Phone::", phone)
    print("Months::", month)
    print("Total price::", total_price)
    print("Bill printed successfully")
    
   
    print("-------------------------------------------------------------------------------------------------")
    
    # Writing the bill in a file
    file = open('bill_' + name + '.txt', 'w')

    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("******************************Techno Property Nepal *********************************************\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Bill\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.write("Land ID:: " + land_id + '\n')
    file.write("Name:: " + name + '\n')
    file.write("Phone:: " + str(phone) + '\n')
    file.write("Months:: " + str(month) + '\n')
    file.write("Total price:: " + str(total_price) + '\n')
    file.write("Bill printed successfully\n")
    file.write("-------------------------------------------------------------------------------------------------\n")
    file.close()

    