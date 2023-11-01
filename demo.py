x = True
login_id = str(input("Enter your login ID:"))
password = str(input("Enter password:"))

while x == True:
    
    if login_id == "Musa" and password == "123456":
        x = False
        print("Login Sucessful")
        x1 = "Order Food"
        x2 = "Breakfast"
        x3 = "Lunch"
        x4 = "Snacks"

        print("1."+x1)
        print("2."+x2)
        print("3."+x3)
        print("4."+x4)

        list = []
        list.append(f"\tName\t\tPrice\tQty\tUnit\tTotal")
        y = True

        while y == True:
            option = int(input("Enter number 1-4 to operate:"))
            if option == 1:
                print("Welcome to order food.")
                y = False
                z = 1
                while z != 0:
                    l1 = str(input("Enter item name:"))
                    l2 = float(input("Enter item price:"))
                    l3 = float(input("Enter item qty:"))
                    l5 = str(input("Enter item unit:"))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to continue and 0 to stop: "))
                    

            elif option == 2:
                print("Welcome to order breakfast.")
                y = False
                z = 1
                while z != 0:
                    l1 = str(input("Enter item name:"))
                    l2 = float(input("Enter item price:"))
                    l3 = float(input("Enter item qty:"))
                    l5 = str(input("Enter item unit:"))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to continue and 0 to stop"))


            elif option == 3:
                print("Welcome to order lunch.")
                y = False
                z = 1
                while z != 0:
                    l1 = str(input("Enter item name:"))
                    l2 = float(input("Enter item price:"))
                    l3 = float(input("Enter item qty:"))
                    l5 = str(input("Enter item unit:"))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = input("Enter 1 to continue and 0 to stop")


            elif option == 4:
                print("Welcome to order snacks.")
                y = False
                z = 1
                while z != 0:
                    l1 = str(input("Enter item name:"))
                    l2 = float(input("Enter item price:"))
                    l3 = float(input("Enter item qty:"))
                    l5 = str(input("Enter item unit:"))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = input("Enter 1 to continue and 0 to stop")
            else:
                print("Invalid entry,try again!")


        if list[1] != "":
            for i in list:
                print(i)

    else:
        print("Login Failed,try again.")
        login_id = str(input("Enter your login ID:"))
        password = str(input("Enter password:"))