def add_item(item, my_list):
    return my_list.append(item)

def remove_item(item, my_list):
    if item not in my_list:
        return "the item not found to remove"
    elif item in my_list:
        return my_list.remove(item)

def display_list(my_list):
    return my_list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_item = input("Enter the item to add: ")
            add_item(user_item, shopping_list)
        elif choice == '2':
            # Prompt for and remove an item
            user_item = input("Enter the item to remove: ")
            remove_item(user_item, shopping_list)
        elif choice == '3':
            # Display the shopping list
           print(display_list(shopping_list))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
