print("\n" * 5)  # Starting after 5x empty lines.

import datetime  # Deltatime library, to get Real Date information.
import os  # OS (Operating system) , To provide cross-platform compatibility
import re   #importing regular expression
list_foods = []  # Variable List of foods, names + prices.
list_drinks = []  # Variable List of drinks, names + prices.
list_services = []  # Variable List of other services, names + prices.

list_item_price = [0] * 100  # Variable List of item prices. Index: 0-39 for foods, index: 40-79 for drinks,
# Index: 80-99 for other services.


navigator_symbol = "/"  # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\"  # This will make the program runnable on Windows


def def_default():
    global list_drinks, list_foods, list_services, list_item_order, list_item_price
    list_item_order = [0] * 100  # Create a list, length 100. Max index number is 99.


def_default()  # Index: 0-39 for foods, index: 40-79 for drinks,
def user():
    while True:
        print("*" * 31 + "Welcome to jiggy" + "*" * 32 + "\n"
                        "\tA complete online food delivery system\n"
                                                         
                                                         
              "(yes or no)  Are you new user?\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        input_1 = str(input("Please Select Your operation"))
        if (input_1 == 'yes'):

            print("\n" * 10)
            print("your name will be considered as id to login this account.so mix it with numbers and charactors")
            input_10 = str(input("enter your name"))
            for i, line in enumerate(open('/home/joseph/Downloads/FoodOrderingSystem/files/users')):
                for match in re.findall(input_10,line):
                    print('You already have an account.Please try again')
                    user()
                break
            file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/users',
                               'a')  # Save it into a file
            file_report.write(input_10)
            file_report.close()
            print('you created an account')
            resturant()  # Start Order Menu function.
            break  # Stop repeating Main Menu.
        elif (input_1 == 'no'):

            print("\n" * 10)  # Create 100 empty lines.
            print("please login your account")
            input2 = str(input("enter your id"))
            for i, line in enumerate(open('/home/joseph/Downloads/FoodOrderingSystem/files/users')):
                for match in re.findall(input2, line):
                    print('You are succesfully logged in')
                    resturant()
            print('your login id is incorrect.Please try again')
            user()




        elif (input_1 == 'E'):

            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
            break  # Stop repeating Main Menu.

        else:
            print("\n" * 10 + "You need to enter either yes or no(" + str(input_1) + "). Try again!")
            user()




def resturant():
    while True:  # Repeat Menu until stops.
        print("*" * 31 + "Resturant" + "*" * 32 + "\n"  # Design for Main Menu.
                                                  "\t(A) Anada Bhavan\n"  # "*" * 31 means, write (*) 31 times.
                                                  "\t(T) Taj\n"
                                                  "\t(L) Le Meridian\n"
                                                  "\t(S) Saravana Bhavan\n"
                                                  "\t(H) Hotel Aryaas\n"
                                                  "\t(E) EXIT\n" +
              "_" * 72)
        input_1 = str(input("Please Select Your Resturant: ")).upper()
        if (len(input_1) == 1):

            if (input_1 == 'A'):

                print("\n" * 10)

                def def_main():
                    while True:
                        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                                  "\t(O) ORDER\n"  # "*" * 31 means, write (*) 31 times.
                                                                  "\t(R) REPORT\n"
                                                                  "\t(P) PAYMENT\n"
                                                                  "\t(A) RESTURANT MENU\n"
                                                                  "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input(
                            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol.
                        if (len(input_1) == 1):  # Checking input length.
                            if (input_1 == 'O'):  # If input is "O".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_order_menu()  # Start Order Menu function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'R'):  # If input is "R".
                                print("\n" * 10)  # Create 100 empty lines.
                                def_report()  # Start Report function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'A'):  # If input is "A".
                                print("\n" * 10)  # Create 10 empty lines.
                                resturant()  # move back to resturant function.
                                break  # Stop repeating Main Menu.

                            elif (input_1 == 'E'):  # If input is "E".
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                                break  # Stop repeating Main Menu.
                            else:  # If O, R, P, E not inserted then...
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Invalid input.
                        else:  # If input length not equal to 1...
                            print(
                                "\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.

                def def_order_menu():
                    while True:  # While looping to keep menu alive
                        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Mail Menu
                                                                   "\t(F) FOODS AND DRINKS\n"
                                                                   "\t(M) MAIN MENU\n"
                                                                   "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options Handling : F-O-M-E.
                        if len(input_1) == 1:
                            if (input_1 == 'F'):  # Easy Access Checking Logic
                                print("\n" * 10)
                                def_food_drink_order()  # Show Food/Drinks Menu
                                break

                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Show Main Menu
                                break
                            elif (input_1 == 'E'):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_full_file_reader():  # mustafa
                    file_foods = open('/home/joseph/Downloads/FoodOrderingSystem/files/anada bhavan/list_foods.fsd',
                                      'r')  # Reading Food List
                    for i in file_foods:  # Line by line reading
                        list_foods.append(str(
                            i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                    file_foods.close()

                    file_drinks = open('/home/joseph/Downloads/FoodOrderingSystem/files/anada bhavan/list_drinks.fsd',
                                       'r')  # Reading Drinks List
                    for i in file_drinks:
                        list_drinks.append(str(i.strip()))
                    file_drinks.close()

                    i = 0
                    while i <= (len(
                            list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
                        if 'RM' in list_foods[i]:
                            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_foods[i].index('RM') - 1)) + str(
                                list_foods[i][list_foods[i].index('RM'):])
                        i += 1

                    i = 0
                    while i <= (len(list_drinks) - 1):
                        if 'RM' in list_drinks[i]:
                            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_drinks[i].index('RM') - 1)) + str(
                                list_drinks[i][list_drinks[i].index('RM'):])
                        i += 1

                def_full_file_reader()

                def def_file_sorter():  # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
                    global list_foods, list_drinks
                    list_foods = sorted(list_foods)
                    list_drinks = sorted(list_drinks)

                    i = 0
                    while i < len(list_foods):
                        list_item_price[i] = float(list_foods[i][int(list_foods[i].index(
                            "RM") + 3):])  # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
                        i += 1

                    i = 0
                    while i < len(list_drinks):
                        list_item_price[40 + i] = float(list_drinks[i][int(
                            list_drinks[i].index(
                                "RM") + 3):])  # Applying extraction on 40 and above items which are the drinks
                        i += 1

                def_file_sorter()

                def def_food_drink_order():
                    while True:
                        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
                        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

                        i = 0
                        while i < len(list_foods) or i < len(list_drinks):
                            var_space = 1
                            if i <= 8:  # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                                var_space = 2

                            if i < len(list_foods):
                                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[
                                                                                           i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
                            else:
                                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
                            if i < len(list_drinks):
                                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                            else:
                                drink = ""
                            print(food, drink)
                            i += 1

                        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

                        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Return to main menu by calling it out
                            break
                        if (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Handling Exit and print out thank you
                            break
                        if (input_1 == 'P'):
                            print("\n" * 10)
                            def_payment()  # Handling payment || More details below
                            break
                        try:  # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                            int(input_1)
                            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(
                                        input_1) - 1]))  # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(
                                        input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass

                                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                                if int(input_2) > 0:
                                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                                    print("\n" * 10)
                                    print("Successfully Ordered!")
                                    def_food_drink_order()  # Return food/drinks Menu
                                    break
                                else:
                                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
                        except:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_report():
                    while True:
                        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
                        file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                           'r').read()  # Reading out reports from report.fsd
                        print(file_report)
                        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
                        input_1 = str(input("Please Select Your Operation: ")).upper()
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Navigate back to menu
                            break
                        elif (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Exit and break up the loop
                            break
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_payment():
                    total=0
                    for x in list_item_order:
                        total=total+x
                    if(total<=20):
                        while True:
                            total_price = 0  # alloc/init a variable to handle total_price

                            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(
                                datetime.datetime.now())[
                                                                                                       :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
                            i = 0
                            while i < len(
                                    list_item_order):  # Enumarating order array items and summing up its prices * quantities
                                if (list_item_order[i] != 0):
                                    if (i >= 0) and (i < 40):
                                        report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[
                                                i])  # string appending the formated food name and formated order structure from quantity and final price
                                        print(" " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[i]))  # print it out
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for food
                                    if (i >= 40) and (i < 80):
                                        report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(
                                            list_item_order[i])
                                        print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for drinks
                                    if (i >= 80) and (i < 100):
                                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                                        print(" " * 17 + str(list_services[i - 80]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for services
                                    i += 1
                                else:
                                    i += 1

                            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)))

                            print(
                                "\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
                            input_1 = str(input("Please Select Your Operation: ")).upper()
                            if (input_1 == 'P'):
                                print("\n" * 10)
                                print("Successfully Paid.Your order is on the way!")
                                file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                                   'a')  # Save it into a file
                                file_report.write(report_new)
                                file_report.close()
                                def_default()  # Reset the program for the name order
                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Navigate back to the main menu
                                break
                            elif (input_1 == 'R'):
                                print("\n" * 10)
                                def_report()  # Navigate to the reports
                                break
                            elif ('E' in input_1) or ('e' in input_1):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
                    else:
                        print("You cannot order more than 20 items in Anada Bhavan")
                        def_main()
                def_main()  # Start Order Menu function.
                break  # Stop repeating Main Menu.
            elif (input_1 == 'T'):
                print("\n" * 10)

                def def_main():
                    while True:  # Repeat Menu until stops.
                        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                                  "\t(O) ORDER\n"  # "*" * 31 means, write (*) 31 times.
                                                                  "\t(R) REPORT\n"
                                                                  "\t(P) PAYMENT\n"
                                                                  "\t(A) RESTURANT MENU\n"
                                                                  "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input(
                            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol.
                        if (len(input_1) == 1):  # Checking input length.
                            if (input_1 == 'O'):  # If input is "O".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_order_menu()  # Start Order Menu function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'R'):  # If input is "R".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_report()  # Start Report function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'P'):  # If input is "P".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_payment()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'A'):  # If input is "P".
                                print("\n" * 10)  # Create 10 empty lines.
                                resturant()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'E'):  # If input is "E".
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                                break  # Stop repeating Main Menu.
                            else:  # If O, R, P, E not inserted then...
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Invalid input.
                        else:  # If input length not equal to 1...
                            print(
                                "\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.

                def def_order_menu():  # yousef
                    while True:  # While looping to keep menu alive
                        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Mail Menu
                                                                   "\t(F) FOODS AND DRINKS\n"
                                                                   "\t(M) MAIN MENU\n"
                                                                   "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options Handling : F-O-M-E.
                        if len(input_1) == 1:
                            if (input_1 == 'F'):  # Easy Access Checking Logic
                                print("\n" * 10)
                                def_food_drink_order()  # Show Food/Drinks Menu
                                break

                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Show Main Menu
                                break
                            elif (input_1 == 'E'):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_full_file_reader():  #
                    file_foods = open('/home/joseph/Downloads/FoodOrderingSystem/files/taj/list_foods.fsd',
                                      'r')  # Reading Food List
                    for i in file_foods:  # Line by line reading
                        list_foods.append(str(
                            i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                    file_foods.close()

                    file_drinks = open('/home/joseph/Downloads/FoodOrderingSystem/files/taj/list_drinks.fsd',
                                       'r')  # Reading Drinks List
                    for i in file_drinks:
                        list_drinks.append(str(i.strip()))
                    file_drinks.close()

                    i = 0
                    while i <= (len(
                            list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
                        if 'RM' in list_foods[i]:
                            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_foods[i].index('RM') - 1)) + str(
                                list_foods[i][list_foods[i].index('RM'):])
                        i += 1

                    i = 0
                    while i <= (len(list_drinks) - 1):
                        if 'RM' in list_drinks[i]:
                            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_drinks[i].index('RM') - 1)) + str(
                                list_drinks[i][list_drinks[i].index('RM'):])
                        i += 1

                def_full_file_reader()

                def def_file_sorter():  # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
                    global list_foods, list_drinks
                    list_foods = sorted(list_foods)
                    list_drinks = sorted(list_drinks)

                    i = 0
                    while i < len(list_foods):
                        list_item_price[i] = float(list_foods[i][int(list_foods[i].index(
                            "RM") + 3):])  # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
                        i += 1

                    i = 0
                    while i < len(list_drinks):
                        list_item_price[40 + i] = float(list_drinks[i][int(
                            list_drinks[i].index(
                                "RM") + 3):])  # Applying extraction on 40 and above items which are the drinks
                        i += 1

                def_file_sorter()

                def def_food_drink_order():
                    while True:
                        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
                        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

                        i = 0
                        while i < len(list_foods) or i < len(list_drinks):
                            var_space = 1
                            if i <= 8:  # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                                var_space = 2

                            if i < len(list_foods):
                                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[
                                                                                           i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
                            else:
                                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
                            if i < len(list_drinks):
                                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                            else:
                                drink = ""
                            print(food, drink)
                            i += 1

                        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

                        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Return to main menu by calling it out
                            break
                        if (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Handling Exit and print out thank you
                            break
                        if (input_1 == 'P'):
                            print("\n" * 10)
                            def_payment()  # Handling payment || More details below
                            break
                        try:  # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                            int(input_1)
                            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(
                                        input_1) - 1]))  # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(
                                        input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass

                                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                                if int(input_2) > 0:
                                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                                    print("\n" * 10)
                                    print("Successfully Ordered!")
                                    def_food_drink_order()  # Return food/drinks Menu
                                    break
                                else:
                                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
                        except:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_report():
                    while True:
                        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
                        file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                           'r').read()  # Reading out reports from report.fsd
                        print(file_report)
                        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
                        input_1 = str(input("Please Select Your Operation: ")).upper()
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Navigate back to menu
                            break
                        elif (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Exit and break up the loop
                            break
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_payment():
                    total = 0
                    for x in list_item_order:
                        total = total + x
                    if (total <=25):
                        while True:
                            total_price = 0  # alloc/init a variable to handle total_price

                            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(
                                datetime.datetime.now())[
                                                                                                       :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
                            i = 0
                            while i < len(
                                    list_item_order):  # Enumarating order array items and summing up its prices * quantities
                                if (list_item_order[i] != 0):
                                    if (i >= 0) and (i < 40):
                                        report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[
                                                i])  # string appending the formated food name and formated order structure from quantity and final price
                                        print(" " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[i]))  # print it out
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for food
                                    if (i >= 40) and (i < 80):
                                        report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(
                                            list_item_order[i])
                                        print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for drinks
                                    if (i >= 80) and (i < 100):
                                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                                        print(" " * 17 + str(list_services[i - 80]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for services
                                    i += 1
                                else:
                                    i += 1

                            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)))

                            print(
                                "\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
                            input_1 = str(input("Please Select Your Operation: ")).upper()
                            if (input_1 == 'P'):
                                print("\n" * 10)
                                print("Successfully Paid.Your order is on the way!")
                                file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                                   'a')  # Save it into a file
                                file_report.write(report_new)
                                file_report.close()
                                def_default()  # Reset the program for the name order
                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Navigate back to the main menu
                                break
                            elif (input_1 == 'R'):
                                print("\n" * 10)
                                def_report()  # Navigate to the reports
                                break
                            elif ('E' in input_1) or ('e' in input_1):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
                    else:
                        print("You cannot order more than 25 items in Taj")
                        def_main()








                def_main()  # Start Report function.
                break  # Stop repeating Main Menu.
            elif (input_1 == 'L'):

                print("\n" * 10)

                def def_main():
                    while True:  # Repeat Menu until stops.
                        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                                  "\t(O) ORDER\n"  # "*" * 31 means, write (*) 31 times.
                                                                  "\t(R) REPORT\n"
                                                                  "\t(P) PAYMENT\n"
                                                                  "\t(A) RESTURANT MENU\n"
                                                                  "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input(
                            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol.
                        if (len(input_1) == 1):  # Checking input length.
                            if (input_1 == 'O'):  # If input is "O".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_order_menu()  # Start Order Menu function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'R'):  # If input is "R".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_report()  # Start Report function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'P'):  # If input is "P".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_payment()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'A'):  # If input is "A".
                                print("\n" * 10)  # Create 10 empty lines.
                                resturant()  # Start resturant function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'E'):  # If input is "E".
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                                break  # Stop repeating Main Menu.
                            else:  # If O, R, P, E not inserted then...
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Invalid input.
                        else:  # If input length not equal to 1...
                            print(
                                "\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.

                def def_order_menu():
                    while True:  # While looping to keep menu alive
                        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Mail Menu
                                                                   "\t(F) FOODS AND DRINKS\n"
                                                                   "\t(M) MAIN MENU\n"
                                                                   "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options Handling : F-O-M-E.
                        if len(input_1) == 1:
                            if (input_1 == 'F'):  # Easy Access Checking Logic
                                print("\n" * 10)
                                def_food_drink_order()  # Show Food/Drinks Menu
                                break

                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Show Main Menu
                                break
                            elif (input_1 == 'E'):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_full_file_reader():  # mustafa
                    file_foods = open('/home/joseph/Downloads/FoodOrderingSystem/files/le meridian/list_foods.fsd',
                                      'r')  # Reading Food List
                    for i in file_foods:  # Line by line reading
                        list_foods.append(str(
                            i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                    file_foods.close()

                    file_drinks = open('/home/joseph/Downloads/FoodOrderingSystem/files/le meridian/list_drinks.fsd',
                                       'r')  # Reading Drinks List
                    for i in file_drinks:
                        list_drinks.append(str(i.strip()))
                    file_drinks.close()

                    i = 0
                    while i <= (len(
                            list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
                        if 'RM' in list_foods[i]:
                            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_foods[i].index('RM') - 1)) + str(
                                list_foods[i][list_foods[i].index('RM'):])
                        i += 1

                    i = 0
                    while i <= (len(list_drinks) - 1):
                        if 'RM' in list_drinks[i]:
                            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_drinks[i].index('RM') - 1)) + str(
                                list_drinks[i][list_drinks[i].index('RM'):])
                        i += 1

                def_full_file_reader()

                def def_file_sorter():  # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
                    global list_foods, list_drinks
                    list_foods = sorted(list_foods)
                    list_drinks = sorted(list_drinks)

                    i = 0
                    while i < len(list_foods):
                        list_item_price[i] = float(list_foods[i][int(list_foods[i].index(
                            "RM") + 3):])  # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
                        i += 1

                    i = 0
                    while i < len(list_drinks):
                        list_item_price[40 + i] = float(list_drinks[i][int(
                            list_drinks[i].index(
                                "RM") + 3):])  # Applying extraction on 40 and above items which are the drinks
                        i += 1

                def_file_sorter()

                def def_food_drink_order():
                    while True:
                        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
                        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

                        i = 0
                        while i < len(list_foods) or i < len(list_drinks):
                            var_space = 1
                            if i <= 8:  # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                                var_space = 2

                            if i < len(list_foods):
                                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[
                                                                                           i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
                            else:
                                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
                            if i < len(list_drinks):
                                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                            else:
                                drink = ""
                            print(food, drink)
                            i += 1

                        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

                        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Return to main menu by calling it out
                            break
                        if (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Handling Exit and print out thank you
                            break
                        if (input_1 == 'P'):
                            print("\n" * 10)
                            def_payment()  # Handling payment || More details below
                            break
                        try:  # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                            int(input_1)
                            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(
                                        input_1) - 1]))  # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(
                                        input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass

                                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                                if int(input_2) > 0:
                                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                                    print("\n" * 10)
                                    print("Successfully Ordered!")
                                    def_food_drink_order()  # Return food/drinks Menu
                                    break
                                else:
                                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
                        except:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_report():
                    while True:
                        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
                        file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                           'r').read()  # Reading out reports from report.fsd
                        print(file_report)
                        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
                        input_1 = str(input("Please Select Your Operation: ")).upper()
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Navigate back to menu
                            break
                        elif (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Exit and break up the loop
                            break
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_payment():
                    total = 0
                    for x in list_item_order:
                        total = total + x
                    if (total <=15):
                        while True:
                            total_price = 0  # alloc/init a variable to handle total_price

                            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(
                                datetime.datetime.now())[
                                                                                                       :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
                            i = 0
                            while i < len(
                                    list_item_order):  # Enumarating order array items and summing up its prices * quantities
                                if (list_item_order[i] != 0):
                                    if (i >= 0) and (i < 40):
                                        report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[
                                                i])  # string appending the formated food name and formated order structure from quantity and final price
                                        print(" " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[i]))  # print it out
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for food
                                    if (i >= 40) and (i < 80):
                                        report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(
                                            list_item_order[i])
                                        print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for drinks
                                    if (i >= 80) and (i < 100):
                                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                                        print(" " * 17 + str(list_services[i - 80]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for services
                                    i += 1
                                else:
                                    i += 1

                            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)))

                            print(
                                "\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
                            input_1 = str(input("Please Select Your Operation: ")).upper()
                            if (input_1 == 'P'):
                                print("\n" * 10)
                                print("Successfully Paid.Your order is on the way!")
                                file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                                   'a')  # Save it into a file
                                file_report.write(report_new)
                                file_report.close()
                                def_default()  # Reset the program for the name order
                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Navigate back to the main menu
                                break
                            elif (input_1 == 'R'):
                                print("\n" * 10)
                                def_report()  # Navigate to the reports
                                break
                            elif ('E' in input_1) or ('e' in input_1):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
                    else:
                        print("You cannot order more than 15 items in Le Meridian")
                        def_main()



                def_main()  # Start Order Menu function.
                break  # Stop repeating Main Menu.



            elif (input_1 == 'H'):

                print("\n" * 10)  # Create 10 empty lines.

                def def_main():
                    while True:  # Repeat Menu until stops.
                        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                                  "\t(O) ORDER\n"  # "*" * 31 means, write (*) 31 times.
                                                                  "\t(R) REPORT\n"
                                                                  "\t(P) PAYMENT\n"
                                                                  "\t(A) RESTURANT MENU\n"
                                                                  "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input(
                            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol.
                        if (len(input_1) == 1):  # Checking input length.
                            if (input_1 == 'O'):  # If input is "O".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_order_menu()  # Start Order Menu function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'R'):  # If input is "R".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_report()  # Start Report function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'P'):  # If input is "P".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_payment()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'A'):  # If input is "A".
                                print("\n" * 10)  # Create 10 empty lines.
                                resturant()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'E'):  # If input is "E".
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                                break  # Stop repeating Main Menu.
                            else:  # If O, R, P, E not inserted then...
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Invalid input.
                        else:  # If input length not equal to 1...
                            print(
                                "\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.

                def def_order_menu():  # yousef
                    while True:  # While looping to keep menu alive
                        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Mail Menu
                                                                   "\t(F) FOODS AND DRINKS\n"
                                                                   "\t(M) MAIN MENU\n"
                                                                   "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options Handling : F-O-M-E.
                        if len(input_1) == 1:
                            if (input_1 == 'F'):  # Easy Access Checking Logic
                                print("\n" * 10)
                                def_food_drink_order()  # Show Food/Drinks Menu
                                break

                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Show Main Menu
                                break
                            elif (input_1 == 'E'):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_full_file_reader():
                    file_foods = open('/home/joseph/Downloads/FoodOrderingSystem/files/Hotel aryaas/list_foods.fsd',
                                      'r')  # Reading Food List
                    for i in file_foods:  # Line by line reading
                        list_foods.append(str(
                            i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                    file_foods.close()

                    file_drinks = open('/home/joseph/Downloads/FoodOrderingSystem/files/Hotel aryaas/list_drinks.fsd',
                                       'r')  # Reading Drinks List
                    for i in file_drinks:
                        list_drinks.append(str(i.strip()))
                    file_drinks.close()

                    i = 0
                    while i <= (len(
                            list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
                        if 'RM' in list_foods[i]:
                            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_foods[i].index('RM') - 1)) + str(
                                list_foods[i][list_foods[i].index('RM'):])
                        i += 1

                    i = 0
                    while i <= (len(list_drinks) - 1):
                        if 'RM' in list_drinks[i]:
                            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_drinks[i].index('RM') - 1)) + str(
                                list_drinks[i][list_drinks[i].index('RM'):])
                        i += 1

                def_full_file_reader()

                def def_file_sorter():  # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
                    global list_foods, list_drinks
                    list_foods = sorted(list_foods)
                    list_drinks = sorted(list_drinks)

                    i = 0
                    while i < len(list_foods):
                        list_item_price[i] = float(list_foods[i][int(list_foods[i].index(
                            "RM") + 3):])  # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
                        i += 1

                    i = 0
                    while i < len(list_drinks):
                        list_item_price[40 + i] = float(list_drinks[i][int(
                            list_drinks[i].index(
                                "RM") + 3):])  # Applying extraction on 40 and above items which are the drinks
                        i += 1

                def_file_sorter()

                def def_food_drink_order():
                    while True:
                        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
                        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

                        i = 0
                        while i < len(list_foods) or i < len(list_drinks):
                            var_space = 1
                            if i <= 8:  # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                                var_space = 2

                            if i < len(list_foods):
                                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[
                                                                                           i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
                            else:
                                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
                            if i < len(list_drinks):
                                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                            else:
                                drink = ""
                            print(food, drink)
                            i += 1

                        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

                        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Return to main menu by calling it out
                            break
                        if (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Handling Exit and print out thank you
                            break
                        if (input_1 == 'P'):
                            print("\n" * 10)
                            def_payment()  # Handling payment || More details below
                            break
                        try:  # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                            int(input_1)
                            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(
                                        input_1) - 1]))  # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(
                                        input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass

                                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                                if int(input_2) > 0:
                                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                                    print("\n" * 10)
                                    print("Successfully Ordered!")
                                    def_food_drink_order()  # Return food/drinks Menu
                                    break
                                else:
                                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
                        except:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_report():
                    while True:
                        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
                        file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                           'r').read()  # Reading out reports from report.fsd
                        print(file_report)
                        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
                        input_1 = str(input("Please Select Your Operation: ")).upper()
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Navigate back to menu
                            break
                        elif (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Exit and break up the loop
                            break
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_payment():
                    total = 0
                    for x in list_item_order:
                        total = total + x
                    if (total <= 20):
                        while True:
                            total_price = 0  # alloc/init a variable to handle total_price

                            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(
                                datetime.datetime.now())[
                                                                                                       :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
                            i = 0
                            while i < len(
                                    list_item_order):  # Enumarating order array items and summing up its prices * quantities
                                if (list_item_order[i] != 0):
                                    if (i >= 0) and (i < 40):
                                        report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[
                                                i])  # string appending the formated food name and formated order structure from quantity and final price
                                        print(" " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[i]))  # print it out
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for food
                                    if (i >= 40) and (i < 80):
                                        report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(
                                            list_item_order[i])
                                        print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for drinks
                                    if (i >= 80) and (i < 100):
                                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                                        print(" " * 17 + str(list_services[i - 80]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for services
                                    i += 1
                                else:
                                    i += 1

                            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)))

                            print(
                                "\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
                            input_1 = str(input("Please Select Your Operation: ")).upper()
                            if (input_1 == 'P'):
                                print("\n" * 10)
                                print("Successfully Paid.Your order is on the way!")
                                file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                                   'a')  # Save it into a file
                                file_report.write(report_new)
                                file_report.close()
                                def_default()  # Reset the program for the name order
                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Navigate back to the main menu
                                break
                            elif (input_1 == 'R'):
                                print("\n" * 10)
                                def_report()  # Navigate to the reports
                                break
                            elif ('E' in input_1) or ('e' in input_1):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
                    else:
                        print("You cannot order more than 20 items in Hotel Aryaas")
                        def_main()


                def_main()  # Start Report function.
                break  # Stop repeating Main Menu.
            elif (input_1 == 'S'):

                print("\n" * 10)  # Create 100 empty lines.

                def def_main():
                    while True:  # Repeat Menu until stops.
                        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                                  "\t(O) ORDER\n"  # "*" * 31 means, write (*) 31 times.
                                                                  "\t(R) REPORT\n"
                                                                  "\t(P) PAYMENT\n"
                                                                  "\t(A) RESTURANT MENU\n"
                                                                  "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input(
                            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol.
                        if (len(input_1) == 1):  # Checking input length.
                            if (input_1 == 'O'):  # If input is "O".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_order_menu()  # Start Order Menu function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'R'):  # If input is "R".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_report()  # Start Report function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'P'):  # If input is "P".
                                print("\n" * 10)  # Create 10 empty lines.
                                def_payment()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'A'):  # If input is "P".
                                print("\n" * 10)  # Create 100 empty lines.
                                resturant()  # Start Payment function.
                                break  # Stop repeating Main Menu.
                            elif (input_1 == 'E'):  # If input is "E".
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                                break  # Stop repeating Main Menu.
                            else:  # If O, R, P, E not inserted then...
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Invalid input.
                        else:  # If input length not equal to 1...
                            print(
                                "\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.

                def def_order_menu():  # yousef
                    while True:  # While looping to keep menu alive
                        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Mail Menu
                                                                   "\t(F) FOODS AND DRINKS\n"
                                                                   "\t(M) MAIN MENU\n"
                                                                   "\t(E) EXIT\n" +
                              "_" * 72)

                        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options Handling : F-O-M-E.
                        if len(input_1) == 1:
                            if (input_1 == 'F'):  # Easy Access Checking Logic
                                print("\n" * 10)
                                def_food_drink_order()  # Show Food/Drinks Menu
                                break

                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Show Main Menu
                                break
                            elif (input_1 == 'E'):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(
                                    input_1) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_full_file_reader():  # mustafa
                    file_foods = open('/home/joseph/Downloads/FoodOrderingSystem/files/saravana bhavan/list_foods.fsd',
                                      'r')  # Reading Food List
                    for i in file_foods:  # Line by line reading
                        list_foods.append(str(
                            i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
                    file_foods.close()

                    file_drinks = open('/home/joseph/Downloads/FoodOrderingSystem/files/saravana bhavan/list_drinks.fsd',
                                       'r')  # Reading Drinks List
                    for i in file_drinks:
                        list_drinks.append(str(i.strip()))
                    file_drinks.close()

                    i = 0
                    while i <= (len(
                            list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
                        if 'RM' in list_foods[i]:
                            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_foods[i].index('RM') - 1)) + str(
                                list_foods[i][list_foods[i].index('RM'):])
                        i += 1

                    i = 0
                    while i <= (len(list_drinks) - 1):
                        if 'RM' in list_drinks[i]:
                            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                                    20 - (list_drinks[i].index('RM') - 1)) + str(
                                list_drinks[i][list_drinks[i].index('RM'):])
                        i += 1

                def_full_file_reader()

                def def_file_sorter():  # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
                    global list_foods, list_drinks
                    list_foods = sorted(list_foods)
                    list_drinks = sorted(list_drinks)

                    i = 0
                    while i < len(list_foods):
                        list_item_price[i] = float(list_foods[i][int(list_foods[i].index(
                            "RM") + 3):])  # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
                        i += 1

                    i = 0
                    while i < len(list_drinks):
                        list_item_price[40 + i] = float(list_drinks[i][int(
                            list_drinks[i].index(
                                "RM") + 3):])  # Applying extraction on 40 and above items which are the drinks
                        i += 1

                def_file_sorter()

                def def_food_drink_order():
                    while True:
                        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
                        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

                        i = 0
                        while i < len(list_foods) or i < len(list_drinks):
                            var_space = 1
                            if i <= 8:  # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                                var_space = 2

                            if i < len(list_foods):
                                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[
                                                                                           i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
                            else:
                                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
                            if i < len(list_drinks):
                                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                            else:
                                drink = ""
                            print(food, drink)
                            i += 1

                        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

                        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Return to main menu by calling it out
                            break
                        if (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Handling Exit and print out thank you
                            break
                        if (input_1 == 'P'):
                            print("\n" * 10)
                            def_payment()  # Handling payment || More details below
                            break
                        try:  # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                            int(input_1)
                            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(
                                        input_1) - 1]))  # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass
                                try:
                                    print("\n" + "_" * 72 + "\n" + str(list_drinks[int(
                                        input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                                except:
                                    pass

                                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                                if int(input_2) > 0:
                                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                                    print("\n" * 10)
                                    print("Successfully Ordered!")
                                    def_food_drink_order()  # Return food/drinks Menu
                                    break
                                else:
                                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
                        except:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_report():
                    while True:
                        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
                        file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                           'r').read()  # Reading out reports from report.fsd
                        print(file_report)
                        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
                        input_1 = str(input("Please Select Your Operation: ")).upper()
                        if (input_1 == 'M'):
                            print("\n" * 10)
                            def_main()  # Navigate back to menu
                            break
                        elif (input_1 == 'E'):
                            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Exit and break up the loop
                            break
                        else:
                            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

                def def_payment():
                    total = 0
                    for x in list_item_order:
                        total = total + x
                    if (total <= 30):
                        while True:
                            total_price = 0  # alloc/init a variable to handle total_price

                            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(
                                datetime.datetime.now())[
                                                                                                       :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
                            i = 0
                            while i < len(
                                    list_item_order):  # Enumarating order array items and summing up its prices * quantities
                                if (list_item_order[i] != 0):
                                    if (i >= 0) and (i < 40):
                                        report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[
                                                i])  # string appending the formated food name and formated order structure from quantity and final price
                                        print(" " * 17 + str(list_foods[i]) + "  x  " + str(
                                            list_item_order[i]))  # print it out
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for food
                                    if (i >= 40) and (i < 80):
                                        report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(
                                            list_item_order[i])
                                        print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for drinks
                                    if (i >= 80) and (i < 100):
                                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                                        print(" " * 17 + str(list_services[i - 80]))
                                        total_price += list_item_price[i] * list_item_order[
                                            i]  # Calculating the total price for services
                                    i += 1
                                else:
                                    i += 1

                            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                                round(total_price, 2)))

                            print(
                                "\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
                            input_1 = str(input("Please Select Your Operation: ")).upper()
                            if (input_1 == 'P'):
                                print("\n" * 10)
                                print("Successfully Paid.Your order is on the way!")
                                file_report = open('/home/joseph/Downloads/FoodOrderingSystem/files/report.fsd',
                                                   'a')  # Save it into a file
                                file_report.write(report_new)
                                file_report.close()
                                def_default()  # Reset the program for the name order
                            elif (input_1 == 'M'):
                                print("\n" * 10)
                                def_main()  # Navigate back to the main menu
                                break
                            elif (input_1 == 'R'):
                                print("\n" * 10)
                                def_report()  # Navigate to the reports
                                break
                            elif ('E' in input_1) or ('e' in input_1):
                                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                                break
                            else:
                                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
                    else:
                        print("You cannot order more than 30 items in Saravana Bhavan")
                        def_main()

                def_main()  # Start Order Menu functEion.
                break  # Stop repeating Main Menu.

            elif (input_1 == 'E'):



                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")  # Good bye comment.
                break

            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input

user()
