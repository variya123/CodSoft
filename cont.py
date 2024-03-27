import json

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, contact in self.contacts.items():
                print(f"Name: {name}, Phone: {contact['phone_number']}")

    def search_contact(self, query):
        for name, contact in self.contacts.items():
            if query.lower() in name.lower() or query in contact['phone_number']:
                print(f"Name: {name}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
                return
        print("Contact not found.")

    def update_contact(self, name, field, new_value):
        if name in self.contacts:
            self.contacts[name][field] = new_value
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()
    contact_manager.load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            field = input("Enter field to update (phone_number, email, address): ")
            new_value = input("Enter new value: ")
            contact_manager.update_contact(name, field, new_value)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            contact_manager.save_contacts()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
