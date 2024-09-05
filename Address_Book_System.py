"""
  @Author: Prayag Bhoir
  @Date: 05-09-2024
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 05-09-2024
  @Title : Address book problem uc1-Ability to create Contacts
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


def main():
    # Create AddressBook instance
    address_book = AddressBook()

    contact_1 = Contact("Prayag", "Bhoir", "Panvel", "Maharashtra", "410206", "8369204930", "Prayagbhoir@gmail.com")

    # Add contacts to the address book
    address_book.add_contact(contact_1)

    # Display all contacts
    address_book.display_contacts()


if __name__ == "__main__":
    main()
