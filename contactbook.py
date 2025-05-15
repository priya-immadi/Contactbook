import csv
import os

FILENAME = 'contacts.csv'

def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, phone, email = row
                contacts[name] = {'phone': phone, 'email': email}
    return contacts

def save_contacts(contacts):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for name, info in contacts.items():
            writer.writerow([name, info['phone'], info['email']])

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"{name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"{name}'s contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__== "__main__":
    main()
