def read(): # Function to display the available lands
    d = {} #Declaring the directory
    file = open('land.txt', 'r') #Opening the file to read the data
    data = file.readlines() #Reading the data from the file
    print("List of lands:") #Displaying the list of lands
    print("-------------------------------------------------------------------------------------------------")
    print("|Land ID\tLocation\tDirection\tAnna\t\tPrice\t\tStatus\t\t|") #Displaying the heading
    print("-------------------------------------------------------------------------------------------------")
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

    for key, value in d.items(): #Iterating through the data
        # Displaying the data
        print('|', key.ljust(9), end='\t')  
        print(value['Location'].ljust(13), end='\t') 
        print(value['Direction'].ljust(13), end='\t')
        print(value['Anna'].ljust(9), end='\t')
        print(value['Price'].ljust(9), end='\t')
        print(value['Status'].ljust(14), end='\t')
        print('|')
    print("-------------------------------------------------------------------------------------------------")
    file.close() #Closing the file to read the data