class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        s
        print(f"Contact {name} added successfully!")

    def view_all_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("All Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter email adress: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
       
        elif choice == '2':
            contact_book.view_all_contacts()
        
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
       
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
