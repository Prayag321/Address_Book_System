"""
  @Author: Prayag Bhoir
  @Date: 05-09-2024
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 06-09-2024
  @Title : Address book problem uc5-Ability to add multiple person
"""
from input_validator import validate_user_input, validate_name, is_email_valid, is_mobile_valid, is_city_valid, is_state_valid, is_zip_code_valid

class Contact:
    def __init__(self, first_name, last_name, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
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
        return (f"\nName:{self.first_name} {self.last_name}\n"
                f"Address: {self.city}, {self.state} {self.zip_code}\n"
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
            print("1. City")
            print("2. State")
            print("3. ZIP Code")
            print("4. Phone")
            print("5. Email")
            print("6. Exit Editing")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.city = input("Enter new city: ")
            elif choice == '2':
                self.state = input("Enter new state: ")
            elif choice == '3':
                self.zip_code = input("Enter new ZIP code: ")
            elif choice == '4':
                self.phone = input("Enter new phone number: ")
            elif choice == '5':
                self.email = input("Enter new email: ")
            elif choice == '6':
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
        self.contacts.append(contact)

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
                print("Contact added successfully!")

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
                print(f"Contact {idx}: {contact}")

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

    return Contact(first_name, last_name, city, state, zip_code, phone, email)

def main():
  # Create AddressBook instance
  address_book = AddressBook()

  while True:
        print("\nAddress Book Menu")
        print("1. Add New Contact")
        print("2. Add Multiple Contacts")
        print("3. Display All Contacts")
        print("4. Edit a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Add new contact
            contact = get_contact_details()
            address_book.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            # Add multiple contacts
            address_book.add_multiple_contacts()
        elif choice == '3':
            # Display all contacts
            address_book.display_contacts()
        elif choice == '4':
            # Edit an existing contact
            address_book.edit_contact_by_name()
        elif choice == '5':
            # Delete an existing contact
            address_book.delete_contact_by_name()
        elif choice == '6':
            # Exit the program
            print("Exiting Address Book.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
