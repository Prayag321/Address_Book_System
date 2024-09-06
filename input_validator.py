"""
  @Author: Prayag Bhoir
  @Date: 05-09-2024
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 06-09-2024
  @Title : Validators for the Address book problem 
"""
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("C:/Users/bhoir/OneDrive/Desktop/pratice_bl/Address_Book_System/input_validator.log"),  # Logs will be saved in this file
    ]
)

def validate_name(name):
    """
    Description:
      This function validates the user name

    Parameters:
      name(str): User input name

    Returns:
      bool:True if match, False otherwise
    """
    pattern = r"^[A-Z][A-Za-z]{1,}$"
    valid = bool(re.match(pattern, name))
    logging.info(f"Validating name: {name} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_email_valid(email):
    """
    Description:
      This function validates the email

    Parameters:
      email(str): User input email

    Returns:
      bool:True if match, False otherwise
    """
    pattern = r"^(?!.*[.@]{2})[a-zA-Z0-9]+([\.\-_]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$"
    valid = bool(re.match(pattern, email))
    logging.info(f"Validating email: {email} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_address_valid(address):
    """
    Description:
      Validates the address input.

    Parameters:
      address (str): The address to be validated.

    Returns:
      bool: True if the address is valid, otherwise False.
    """
    pattern = r"^[a-zA-Z0-9\s,.-]{5,}$"
    valid = bool(re.match(pattern, address))
    logging.info(f"Validating city: {address} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_city_valid(city):
    """
    Description:
      This function validates the city name

    Parameters:
      city(str): User input city name

    Returns:
      bool: True if match, False otherwise
    """
    pattern = r"^[A-Za-z]+$"
    valid = bool(re.match(pattern, city))
    logging.info(f"Validating city: {city} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_state_valid(state):
    """
    Description:
      This function validates the state name

    Parameters:
      state(str): User input state name

    Returns:
      bool: True if match, False otherwise
    """
    pattern = r"^[A-Za-z]+$"
    valid = bool(re.match(pattern, state))
    logging.info(f"Validating state: {state} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_zip_code_valid(zip_code):
    """
    Description:
      This function validates the ZIP code

    Parameters:
      zip_code(str): User input ZIP code

    Returns:
      bool: True if match, False otherwise
    """
    pattern = r"^\d{6}$"
    valid = bool(re.match(pattern, zip_code))
    logging.info(f"Validating ZIP code: {zip_code} - {'Valid' if valid else 'Invalid'}")
    return valid

def is_mobile_valid(mobile):
    """
    Description:
      This function validates the mobile number

    Parameters:
      mobile(str): User input mobile number

    Returns:
      bool: True if match, False otherwise
    """
    pattern = r"^\d{2} \d{10}$"
    valid = bool(re.match(pattern, mobile))
    logging.info(f"Validating mobile number: {mobile} - {'Valid' if valid else 'Invalid'}")
    return valid

def validate_user_input(input_prompt, validation_func, success_message, failure_message):
    """
    Description:
      This function handles the validation of user input.

    Parameters:
      input_prompt(str): The prompt to be displayed to the user.
      validation_func(func): The function that validates the input.
      success_message(str): The message to display on successful validation.
      failure_message(str): The message to display on failed validation.

    Returns:
      user_input: valid user input.
    """
    while True:
        user_input = input(input_prompt)
        if validation_func(user_input):
            logging.info(success_message)
            print("  **",success_message)
            return user_input  # Valid input
        else:
            logging.warning(failure_message)
            print("  **",failure_message)


def main():
  pass

if __name__ == "__main__":
    main()
