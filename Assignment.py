#Minh Tran, CP 1404 Assignment 1, Github link: 

#function menu:
def menu():
    while True:
        print("(L)ist all items")
        print("(H)ire an item")
        print("(R)eturn an item")
        print("(A)dd new item to stock")
        print("(Q)uit")
        menu_selection = input(str(">>> "))
        if menu_selection == "L" or menu_selection == 'l':
            item_list()
        elif menu_selection == "H" or menu_selection == 'h':
            item_hire()
        elif menu_selection == "R" or menu_selection == 'r':
            item_return()
        elif menu_selection == "A" or menu_selection == 'a':
            item_add()
        elif menu_selection == "Q" or menu_selection == 'q':
            print("Have a nice day")
        break
    else:
        print("Invalid menu choice")
    return menu()

#function item_list
def item_list():
    while True:
        print("All item on file: ")
        list1 = [ "Rusty Bucket (40L bucket - quite rusty)"];
        list2 = ["Golf Cart (Tesla powered 250 turbo)"];
        list3 = ["Thermomix (TM-31)"];
        list4 = ["$0.00"];
        list5 = ["$195.00"];
        list6 = ["$25.50"];
        list_selection = input(str(">>> "))
        if list_selection == "0":
            print(list1 + list4)
        elif list_selection == "1":
            print(list2 + list5)
        elif list_selection == "2":
            print (list3 + list6)
        break
    else:
        print("Invalid")
    return item_list()

#function item_hire
def item_hire():
     while True:
        list1 = [ "Rusty Bucket (40L bucket - quite rusty)"];
        list2 = ["Golf Cart (Tesla powered 250 turbo)"];
        list3 = ["Thermomix (TM-31)"];
        list4 = ["$0.00"];
        list5 = ["$195.00"];
        list6 = ["$25.50"];
        list_selection = input(str(">>> "))
        if list_selection == 'H' or list_selection == 'h':
            print (list1 + list4)
            print (list2 + list5)
            del (list3);
            del (list6);
        break
        if list_selection == '0':
            print (list1, 'is hired for', list6)
        elif list_selection == '1':
            print (list2, 'is hired for', list5)

        break
     else:
         print('Invalid')

     return item_hire()


#function item_return()
    def item_return():








