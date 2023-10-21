# Define a list to store contacts
contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print(f"{name} has been added to your contacts.")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")
def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found_contacts = []

    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")
def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    found_contacts = []

    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

        choice = input("Enter the number of the contact to update: ")

        try:
            index = int(choice) - 1
            if 0 <= index < len(found_contacts):
                contact = found_contacts[index]
                print(f"Updating contact: {contact['Name']}")
                contact["Name"] = input("Enter the new name: ")
                contact["Phone"] = input("Enter the new phone number: ")
                contact["Email"] = input("Enter the new email: ")
                contact["Address"] = input("Enter the new address: ")
                print("Contact updated successfully.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    found_contacts = []

    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

        choice = input("Enter the number of the contact to delete: ")

        try:
            index = int(choice) - 1
            if 0 <= index < len(found_contacts):
                contact = found_contacts[index]
                print(f"Deleting contact: {contact['Name']}")
                contacts.remove(contact)
                print("Contact deleted successfully.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Main loop for the contact book
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
