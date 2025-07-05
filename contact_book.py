# Contact Book

# Step 1:Initalize an empty contact book
contacts = {}

# Step 2: Menüyü göster


def show_menu():
    print("Contact Book Menu:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Quit")


# Step 3: Add a Contact


def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email of the contact: ")
    if name in contacts:
        print(f"The contact {name} already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} has been added successfully!")
# Step 4:Show Contacts


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for person, details in contacts.items():
            print(
                f"Name: {person}, Phone: {details['phone']}, Email: {details['email']}")

# Step 5: Search a Contact


def search_contact():
    person = input("Enter the name of the contact you want to search: ")
    if person in contacts:
        print(f"Name: {person}")
        print(f"Phone: {contacts[person]['phone']}")
        print(f"Email: {contacts[person]['email']}")
    else:
        print(f"The contact {person} is not exist")

# Step 6: Edit a Contact


def edit_contact():

    print("Available contacts:")
    for person in contacts.keys():
        print(f"- {person}")
    person = input("Enter the of contact you want to edit :")
    if person in contacts:
        print(f"\nEditing contact {person}:")
        print("1. Edit Phone")
        print("2. Edit Email")
        choice = input("Choose an option (1 or 2): ")
        if choice == "1":
            new_phone = input("Enter the new phone number: ")
            contacts[person]['phone'] = new_phone
            print(f"Phone number for {person} has been updated.")
        elif choice == "2":
            new_email = input("Enter the new email: ")
            contacts[person]['email'] = new_email
            print(f"Email for {person} has been updated.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print(f"The contact {person} does not exist.")


# Step 7: Delete a Contact

def delete_contact():
    person = input("Enter the name of the contact you want to delete: ")
    if person in contacts:
        del contacts[person]
        print(f"Contact {person} has been deleted successfully!")
    else:
        print(f"The contact {person} does not exist.")


# Step 8: Quit the program
def quit_program():
    print("Exiting the Contact Book. Goodbye!")
    exit()


# Step 9: Main loop to run the contact book
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            quit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
# This code implements a simple contact book application with functionalities to view, add, search, edit, and delete contacts.
# It uses a dictionary to store contacts, where each contact's details are stored as a nested dictionary.
# The program runs in a loop, allowing users to choose options from a menu until they decide to quit the application.
# The contact book is initialized as an empty dictionary, and the user can interact with it through a text-based menu interface.
