# ContactMaster - Simple Contact Management CLI App

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    notes = input("Enter notes: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Notes": notes
        }
        print(f"Contact '{name}' added successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"\nName: {name}")
        for key, value in contact.items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        for key, value in details.items():
            print(f"{key}: {value}")

def main():
    while True:
        print("\n==== ContactMaster ====")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting ContactMaster. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
