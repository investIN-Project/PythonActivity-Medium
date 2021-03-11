# LOOK FOR "ACTIVITY HERE" COMMENTS


# importing mysql library
from mysql.connector import connect, Error

# establishing connection to mysql database with try catch statement
try:
    connection = connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="r5dkjtl8xh7ips5z",
        password="zitx2h253jmyxbre",
        database="d19f7icboqgje0ck",
    )
except Error as e:
    print(e)

# initailising all variables
cursor = connection.cursor()
possibleCommands = ["help", "add item", "quit", "list items", "search item", "sort list"]

# starting a while loop to iterate through commands
while True:
    # converting entered command to lower case
    command = input("Please enter command: ").strip().lower()

    # checking if command is equal to "quit"
    if command == possibleCommands[3]:
        # Displaying "bye" message and closing program

        # ACTIVITY HERE
        # print goodbye message

        print("")
        exit()

    # checking if command is equal to "help"
    elif command == possibleCommands[0]:
        # printing all supported commands
        print("Possible Commands:", possibleCommands)
        print("")

    # checking if command is equal to "list items"
    elif command == possibleCommands[4]:
        # running sql query to retrive item list

        # ACTIVITY HERE
        # Please insert list item (select) sql command here
        sql_select_Query = ""

        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # printing item list with for loop
        print("List of available items:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]))
        print("")

    # checking if command is equal to "add item"
    elif command == possibleCommands[1]:
        # taking new item name as input
        NewItemName = input("Please enter new item name: ")
        # inserting new item into database
        
        # ACTIVITY HERE
        # Please insert add item (insert) sql command here
        sql = ""

        val = ("NULL", NewItemName)
        cursor.execute(sql, val)
        connection.commit()
        # running sql query to retrive updated item list

        # ACTIVITY HERE
        # Please insert list item (select) sql command here
        sql_select_Query = ""
        
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # printing updated item list with for loop
        print("Updated List of available items:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]))
        print("")

    # checking if command is equal to "search item"
    elif command == possibleCommands[5]:
        # taking input for search
        searchKey = input("Type here to search for items: ")
        # running sql query to retrive item list where item name is like entered string
        sql = """SELECT * FROM items WHERE itemName LIKE %s"""
        adr = ("%"+searchKey+"%", )
        cursor.execute(sql, adr)
        records = cursor.fetchall()
        # printing search results
        print("Search result:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]))
        print("")
    
    # checking if command is equal to "sort list"
    elif command == possibleCommands[6]:
        # printing possible sorting options
        print("Please choose sorting type: \n1 - ID Ascending\n2 - ID Descending\n3 - Name Ascending\n4 - Name Descending")
        # taking sort type as input
        sortID = input("Please enter sort type (number): ").strip().lower()
        # checking if sort type 1 is chosen
        if sortID == "1":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from items ORDER BY itemID"
            cursor.execute(sql_select_Query)
        # checking if sort type 2 is chosen
        if sortID == "2":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from items ORDER BY itemID DESC"
            cursor.execute(sql_select_Query)
        # checking if sort type 3 is chosen
        if sortID == "3":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from items ORDER BY itemName"
            cursor.execute(sql_select_Query)
        # checking if sort type 4 is chosen
        if sortID == "4":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from items ORDER BY itemName DESC"
            cursor.execute(sql_select_Query)
        # fetching queried data
        records = cursor.fetchall()
        # printing item list with for loop
        print("Ascending List of available items:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]))
        print("")

    # If no valid commands are entered
    else:
        # Error message, for invalid command
        # printing all supported commands

        # ACTIVITY HERE
        # print error message here and all possible commands (use seperate print statements)
        
        print("")