def choice_():
    print("-------------------------------------------------------------------------------------------------")
    print("******************************Techno Property Nepal *********************************************")
    print("-------------------------------------------------------------------------------------------------")
    print("Provided facilities::")
    print("1. Rent lands")
    print("2. Return rented lands")
    print("3. Exit")

def design():
    print("-------------------------------------------------------------------------------------------------")
    print("******************************Techno Property Nepal *********************************************")
    print("-------------------------------------------------------------------------------------------------")

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
                d[land_id]['Status'] = 'Not_Available'
                print("Land rented successfully")
            else:
                print("Land is already rented")
        else:
            print("Land ID not found")
    except ValueError:
        print("Invalid input")
    file.close()