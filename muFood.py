print("Welcome To MU Food Library")
x = True
login_Id = str(input("Enter Login ID: "))
password = str(input("Enter Password: "))

while x == True:
    if login_Id == "Musa" and password == "1234":
        x = False
        print("Login Successful")
        x1 = "Order Food"
        x2 = "Breakfast"
        x3 = "Lunch"
        x4 = "Snacks"
        
        print("\nChoose Your Option")
        print("1: "+x1)
        print("2: "+x2)
        print("3: "+x3)
        print("4: "+x4)

        list = []
        list.append(f"\tName\t\tPrice\tQty\tUnit\tTotal")
        y = True

        while y == True:
            option = int(input("\nEnter Number 1-4 to operate: "))
            if option == 1:
                print("\nHey Foodie! Order Food Now :)")
                print("Available Items\n=> Chicken Biriyani = 160/=\n=> Kacci Biriyani = 290/=\n=> Egg Pulao = 60/=\n")
                y = False
                z = 1
                while z!=0:
                    l1 = str(input("Enter Item Name: "))
                    l2 = float(input("Enter Item Price: "))
                    l3 = int(input("Enter Item Qty: "))
                    l5 = str(input("Enter Item Unit: "))
                    l4 = int(input(l2*l3))

                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to Continue and ) to Stop"))

            elif option == 2:
                print("Lets Enjoy Fresh and Healthy Breakfast :)")
                y = False
                z = 1
                while z!=0:
                    l1 = str(input("Enter Item Name: "))
                    l2 = float(input("Enter Item Price: "))
                    l3 = int(input("Enter Item Qty: "))
                    l5 = str(input("Enter Item Unit: "))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to Continue and 0 to Stop"))

            elif option == 3:
                print("OOh! Lets Complete Most Important Meal Of the day")
                y = False
                z = 1
                while z!=0:
                    l1 = str(input("Enter Item Name: "))
                    l2 = float(input("Enter Item Price: "))
                    l3 = int(input("Enter Item Qty: "))
                    l5 = str(input("Enter Item Unit: "))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to Continue and 0 to Stop"))

            elif option == 4:
                print("Lets Taste City's Famous Snacks:)")
                y = False
                z = 1
                while z!=0:
                    l1 = str(input("Enter Item Name: "))
                    l2 = float(input("Enter Item Price: "))
                    l3 = int(input("Enter Item Qty: "))
                    l5 = str(input("Enter Item Unit: "))
                    l4 = int(l2*l3)
                    list.append(f"\t{l1}\t\t{l2}\t{l3}\t{l5}\t{l4}")
                    z = int(input("Enter 1 to Continue and 0 to Stop"))

            else:
                print("Invalid entry, try again!!!")
        if list[1]!="":
            for i in list:
                print(i)
        
        else:
            print("Login Failed, Try Again.")
            login_Id = str(input("Enter Your Id:"))
            password = str(input("Enter Password:"))


