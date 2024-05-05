# Create a function such taht it will update the status of the land to Not_Available in the file land.txt
def update_status(Id):
    d = {} #Declaring the directory
    file = open('land.txt', 'r')#Opening the file to read the data
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
    for key , value in d.items():
        if(Id == key):
            value['Status'] = 'Not_Available'#Changing the status of land as not available
            break
    file.close()#Closing the file
    
    file = open('land.txt', 'w')
    for key , value in d.items():
        # Updating the data
        file.write(key + ' ' + value['Location'] + ' ' + value['Direction'] + ' ' + value['Anna'] + ' ' + value['Price'] + ' ' + value['Status'] + '\n')
    file.close()

def update_returnStatus(Id):
    d={}#Declaring directory
    file = open('land.txt','r')#Opening file to read the data
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
    
    #Checking the id of land 
    for key, value in d.items():
        if(Id == key):
            value['Status'] = 'Available' #Changing the status of the land to available
            break
    file.close()

    # Opening file to update the data
    file = open('land.txt','w')
    for key, value in d.items():
        # Updating the data
        file.write(key + ' ' + value['Location'] + ' ' + value['Direction'] + ' ' + value['Anna'] + ' ' + value['Price'] + ' ' + value['Status'] + '\n')
    file.close()#Closing the file
