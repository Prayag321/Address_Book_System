"""
  @Author: Prayag Bhoir
  @Date: 05-09-2024
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 08-09-2024
  @Title : Address book problem uc12-sort by city
"""
from input_validator import validate_user_input, validate_name,is_address_valid, is_email_valid, is_mobile_valid, is_city_valid, is_state_valid, is_zip_code_valid

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Description:
          Returns a string representation of the contact while printing object.

        Parameters:
          None

        Returns:
          str: The formatted string with contact details.
        """
        return (f"\nName: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
                f"Phone: {self.phone}, Email: {self.email}")

    def edit_contact(self):
        """
        Description:
          Provides a menu to edit specific contact fields.

        Parameters:
          None

        Returns:
          None
        """
        while True:
            print("\nWhat would you like to edit?")
            print("1. Address")
            print("2. City")
            print("3. State")
            print("4. ZIP Code")
            print("5. Phone")
            print("6. Email")
            print("7. Exit Editing")
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.address = input("Enter new address: ")
            elif choice == '2':
                self.city = input("Enter new city: ")
            elif choice == '3':
                self.state = input("Enter new state: ")
            elif choice == '4':
                self.zip_code = input("Enter new ZIP code: ")
            elif choice == '5':
                self.phone = input("Enter new phone number: ")
            elif choice == '6':
                self.email = input("Enter new email: ")
            elif choice == '7':
                print("Exiting edit mode.")
                break
            else:
                print("Invalid choice. Please try again.")



class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
          Adds a new contact to the address book.

        Parameters:
          contact (Contact): The contact to be added.

        Returns:
          None
        """
        if self.find_contact_by_name(contact.first_name, contact.last_name):
            print(f"A contact with the name {contact.first_name} {contact.last_name} already exists.")
        else:
            self.contacts.append(contact)
            print("Contact added successfully!")

    def add_multiple_contacts(self):
            """
            Description:
              Allows the user to add multiple contacts at once.

            Parameters:
              None

            Returns:
              None
            """
            num_contacts = int(input("How many contacts would you like to add? "))
            for _ in range(num_contacts):
                contact = get_contact_details()
                self.add_contact(contact)
                # print("Contact added successfully!")

    def display_contacts(self):
        """
        Description:
          Displays all contacts in the address book.

        Parameters:
          None

        Returns:
          None
        """
        if not self.contacts:
            print("Address book is empty.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {idx}: {contact}")

    def find_contact_by_name(self, first_name, last_name):
        """
        Description:
          Finds a contact in the address book by first and last name.

        Parameters:
          first_name (str): The first name of the contact.
          last_name (str): The last name of the contact.

        Returns:
          Contact: The contact if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def edit_contact_by_name(self):
        """
        Description:
          Searches for a contact by name and allows editing if found.

        Parameters:
          None

        Returns:
          None
        """
        first_name = input("Enter the first name of the contact to edit: ")
        last_name = input("Enter the last name of the contact to edit: ")

        contact = self.find_contact_by_name(first_name, last_name)

        if contact:
            print(f"Editing contact: {contact}")
            contact.edit_contact()
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact_by_name(self):
          """
          Description:
            Deletes a contact from the address book by name.

          Parameters:
            None

          Returns:
            None
          """
          first_name = input("Enter the first name of the contact to delete: ")
          last_name = input("Enter the last name of the contact to delete: ")

          contact = self.find_contact_by_name(first_name, last_name)

          if contact:
              self.contacts.remove(contact)
              print(f"Contact {first_name} {last_name} deleted successfully!")
          else:
              print("Contact not found.")

def search_person_in_city(address_books):
    """
    Description:
      Searches for a person in a specific city across multiple address books.

    Parameters:
      address_books (dict): A dictionary of address books with their names as keys.

    Returns:
      None
    """
    city = input("Enter the city to search: ")
    first_name = input("Enter the first name of the person: ")
    last_name = input("Enter the last name of the person: ")

    found = False

    for book_name, address_book in address_books.items():
        for contact in address_book.contacts:
            if contact.first_name == first_name and contact.last_name == last_name and contact.city == city:
                print(f"\nPerson found in Address Book '{book_name}':")
                print(contact)
                found = True

    if not found:
        print(f"No person named {first_name} {last_name} found in city {city} across all address books.")

def view_persons_by_state(address_books):
    """
    Description:
      Displays all persons residing in a specific state across all address books.

    Parameters:
      address_books (dict): A dictionary of address books with their names as keys.

    Returns:
      None
    """
    state = input("Enter the state to search: ")

    found = False

    for book_name, address_book in address_books.items():
        for contact in address_book.contacts:
            if contact.state == state:
                if not found:
                    print(f"\nPeople found in the state '{state}':")
                print(f"\nIn Address Book '{book_name}':")
                print(contact)
                found = True

    if not found:
        print(f"No persons found in state {state} across all address books.")

def count_persons_by_state(address_books):
    """
    Description:
      Counts the number of persons residing in a specific state across all address books.

    Parameters:
      address_books (dict): A dictionary of address books with their names as keys.

    Returns:
      None
    """
    state = input("Enter the state to count persons: ")

    total_count = 0

    for book_name, address_book in address_books.items():
        state_count = sum(1 for contact in address_book.contacts if contact.state == state)
        if state_count > 0:
            print(f"In Address Book '{book_name}', {state_count} persons found in the state '{state}'.")
        total_count += state_count

    if total_count > 0:
        print(f"\nTotal number of persons in state '{state}' across all address books: {total_count}")
    else:
        print(f"No persons found in state {state} across all address books.")

def sort_contacts_by_name(address_book):
    """
    Description:
      Sorts the contacts in the address book alphabetically by the person's first and last name.

    Parameters:
      address_book (AddressBook): The address book instance whose contacts will be sorted.

    Returns:
      None
    """
    if not address_book.contacts:
        print("Address book is empty.")
    else:
        # Sort contacts based on first name, then last name
        sorted_contacts = sorted(address_book.contacts, key=lambda contact: (contact.first_name, contact.last_name))
        print("\nContacts sorted alphabetically by name:")
        for idx, contact in enumerate(sorted_contacts, start=1):
            print(f"\nContact {idx}: {contact}")

def sort_contacts_by_city(address_book):
    """
    Description:
      Sorts the contacts in the address book by city name in alphabetical order.

    Parameters:
      address_book (AddressBook): The address book instance whose contacts will be sorted.

    Returns:
      None
    """
    if not address_book.contacts:
        print("Address book is empty.")
    else:
        # Sort contacts based on city name
        sorted_contacts = sorted(address_book.contacts, key=lambda contact: contact.city)
        print("\nContacts sorted by City:")
        for idx, contact in enumerate(sorted_contacts, start=1):
            print(f"\nContact {idx}: {contact}")

def get_contact_details():
    """
    Description:
      Collects contact details from the console and validates the input using the validation module.

    Parameters:
      None

    Returns:
      Contact: A new Contact object created with user input.
    """
    first_name = validate_user_input(
        "Enter First Name (must start with an uppercase letter and be at least 2 characters long): ",
        validate_name,
        "First name is valid.",
        "Invalid first name. Please try again."
    )
    if first_name is None:
        return

    last_name = validate_user_input(
        "Enter Last Name (must start with an uppercase letter and be at least 2 characters long): ",
        validate_name,
        "Last name is valid.",
        "Invalid last name. Please try again."
    )
    if last_name is None:
        return
    
    address = validate_user_input(
        "Enter Address (must be at least 5 characters long and not contain special characters): ",
        is_address_valid,
        "Address is valid.",
        "Invalid address. Please try again."
    )
    if address is None:
        return

    city = validate_user_input(
        "Enter City: ",
        is_city_valid,
        "City name is valid.",
        "Invalid city name. Please try again."
    )
    if city is None:
        return

    state = validate_user_input(
        "Enter State: ",
        is_state_valid,
        "State name is valid.",
        "Invalid state name. Please try again."
    )
    if state is None:
        return

    zip_code = validate_user_input(
        "Enter ZIP Code: ",
        is_zip_code_valid,
        "ZIP code is valid.",
        "Invalid ZIP code. Please try again."
    )
    if zip_code is None:
        return

    phone = validate_user_input(
        "Enter Phone Number (format: XX XXXXXXXXXX): ",
        is_mobile_valid,
        "Phone number is valid.",
        "Invalid phone number. Please try again."
    )
    if phone is None:
        return

    email = validate_user_input(
        "Enter Email: ",
        is_email_valid,
        "Email is valid.",
        "Invalid email address. Please try again."
    )
    if email is None:
        return

    return Contact(first_name, last_name, address, city, state, zip_code, phone, email)

def main():
    address_books = {}  # Dictionary to hold address books by name

    while True:
        print("\nMain Menu")
        print("1. Add New Address Book")
        print("2. Select Address Book")
        print("3. Search Person in City Across Address Books")
        print("4. View Persons by State Across Address Books")
        print("5. Count Persons by State Across Address Books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Add new address book
            name = input("Enter the name for the new address book: ")
            if name in address_books:
                print("Address book with this name already exists.")
            else:
                # Create AddressBook instance
                address_books[name] = AddressBook()
                print(f"Address book '{name}' created successfully!")

        elif choice == '2':
            for key, _ in address_books.items():
                print(key)
            # Select an address book
            name = input("Enter the name of the address book to select: ")
            if name not in address_books:
                print("Address book not found.")
                continue

            address_book = address_books[name]

            while True:
                print(f"\nAddress Book Menu for '{name}'")
                print("1. Add New Contact")
                print("2. Add Multiple Contacts")
                print("3. Display All Contacts")
                print("4. Edit a Contact")
                print("5. Delete a Contact")
                print("6. Sort Contacts Alphabetically by Name")
                print("7. Sort Contacts by City")
                print("8. Back to Main Menu")
                sub_choice = input("Enter your choice (1-8): ")

                if sub_choice == '1':
                    # Add new contact
                    contact = get_contact_details()
                    if contact:
                        address_book.add_contact(contact)
                elif sub_choice == '2':
                    # Add multiple contacts
                    address_book.add_multiple_contacts()
                elif sub_choice == '3':
                    # Display all contacts
                    address_book.display_contacts()
                elif sub_choice == '4':
                    # Edit an existing contact
                    address_book.edit_contact_by_name()
                elif sub_choice == '5':
                    # Delete an existing contact
                    address_book.delete_contact_by_name()
                elif sub_choice == '6':
                    # Sort contacts alphabetically by name
                    sort_contacts_by_name(address_book)
                elif sub_choice == '7':
                    # Sort contacts by City
                    sort_contacts_by_city(address_book)
                elif sub_choice == '8':
                    # Back to main menu
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            # Search for a person in a city across multiple address books
            search_person_in_city(address_books)

        elif choice == '4':
            # View persons by state across multiple address books
            view_persons_by_state(address_books)

        elif choice == '5':
            # Count persons by state across multiple address books
            count_persons_by_state(address_books)

        elif choice == '6':
            # Exit the program
            print("Exiting Address Book System.")
            break

        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()
