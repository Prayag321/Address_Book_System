"""
  @Author: Prayag Bhoir
  @Date: 05-09-2024
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 05-09-2024
  @Title : Address book problem uc2-Ability to add a new contact
"""
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

def get_contact_details():
    """
    Description:
      Collects contact details from the console and returns a Contact object.
    Parameters:
      None
    Returns:
      Contact: A new Contact object created with user input.
    """
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zip_code = input("Enter ZIP Code: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    return Contact(first_name, last_name, city, state, zip_code, phone, email)

def main():
  # Create AddressBook instance
  address_book = AddressBook()

  while True:
      print("\nAddress Book Menu")
      print("1. Add New Contact")
      print("2. Display All Contacts")
      print("3. Exit")
      choice = input("Enter your choice (1-3): ")

      if choice == '1':
          # Add new contact
          contact = get_contact_details()
          address_book.add_contact(contact)
          print("Contact added successfully!")
      elif choice == '2':
          # Display all contacts
          address_book.display_contacts()
      elif choice == '3':
          # Exit the program
          print("Exiting Address Book.")
          break
      else:
          print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
