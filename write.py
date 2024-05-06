# Create a function such taht it will update the status of the land to Not_Available in the file land.txt
def update_status(Id): 
    d = {} #Declaring the directory
    file = open('land.txt', 'r')#Opening the file to read the data
    data = file.readlines() #Reading the data from the file
    for line in data: #Iterating through the data
        col = line.split() #Splitting the data
        key = col[0] #Assigning the key
        value = { #Assigning the value
            'Location': col[1],
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value #Assigning the value to the key
    for key , value in d.items(): #Iterating through the data
        if(Id == key): #Checking the id of the land
            value['Status'] = 'Not_Available'#Changing the status of land as not available
            break #Breaking the loop
    file.close()#Closing the file to read the data
    
    file = open('land.txt', 'w') #Opening the file to write the data
    for key , value in d.items(): #Iterating through the data
        # Updating the data
        file.write(key + ' ' + value['Location'] + ' ' + value['Direction'] + ' ' + value['Anna'] + ' ' + value['Price'] + ' ' + value['Status'] + '\n')
    file.close() #Closing the file to write the data

# Create a function such that it will update the status of the land to Available in the file land.txt
def update_returnStatus(Id): 
    d={}#Declaring directory
    file = open('land.txt','r')#Opening file to read the data
    data = file.readlines() #Reading the data from the file
    for line in data: #Iterating through the data
        col = line.split() #Splitting the data
        key = col[0] #Assigning the key
        value = { #Assigning the value
            'Location': col[1],
            'Direction': col[2],
            'Anna': col[3],
            'Price': col[4],
            'Status': ' '.join(col[5:])
        }
        d[key] = value #Assigning the value to the key
    
    #Checking the id of land 
    for key, value in d.items(): #Iterating through the data
        if(Id == key): #Checking the id of the land
            value['Status'] = 'Available' #Changing the status of the land to available
            break #Breaking the loop
    file.close() #Closing the file to read the data

    # Opening file to update the data
    file = open('land.txt','w') #Opening the file to write the data
    for key, value in d.items():  #Iterating through the data
        # Updating the data
        file.write(key + ' ' + value['Location'] + ' ' + value['Direction'] + ' ' + value['Anna'] + ' ' + value['Price'] + ' ' + value['Status'] + '\n')
    file.close()#Closing the file
