
done = 1
selection = 0
todo_list = []
holder = ''
n = 0
while done != 0:
    
    selection = input("What would you like todo? \n(1) Add Item\n(2) View List\n(3) Exit\n")
    if selection == '3':
        done = 0
    elif selection == '1':
        holder = input("What would you like to add?")
        todo_list.append(holder)
        print("\nAdded!\n")
    elif selection == '2':
        if len(todo_list) == 0:
            print("Please Add Items To List Before Viewing!")
        else:
            print("Your List:\n")
            while n != len(todo_list):
                print(todo_list[n])
                n = n + 1
            n = 0
            print()
    else:
        print("Please Enter A Menu Item")
