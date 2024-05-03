def read():
    d = {}
    file = open('land.txt', 'r')
    data = file.readlines()
    print("List of lands:")
    print("-------------------------------------------------------------------------------------------------")
    print("|Land ID\tLocation\tDirection\tAnna\t\tPrice\t\tStatus\t\t|")
    print("-------------------------------------------------------------------------------------------------")
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

    for key, value in d.items():
        print('|', key.ljust(9), end='\t')
        print(value['Location'].ljust(13), end='\t')
        print(value['Direction'].ljust(13), end='\t')
        print(value['Anna'].ljust(9), end='\t')
        print(value['Price'].ljust(9), end='\t')
        print(value['Status'].ljust(14), end='\t')
        print('|')
    print("-------------------------------------------------------------------------------------------------")
    file.close()

