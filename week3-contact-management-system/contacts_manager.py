# ==========================================
# Contact Management System
# Week 3 Project - Functions & Dictionaries
# ==========================================

import json
import re
from datetime import datetime
import csv


# ---------- Function to check phone number ----------
# This function removes extra characters
# and checks if the number has 10 to 15 digits
def check_phone_number(phone_input):
    # Remove everything except digits
    only_digits = re.sub(r"\D", "", phone_input)

    if 10 <= len(only_digits) <= 15:
        return True, only_digits
    else:
        return False, None


# ---------- Function to check email format ----------
# This function checks if email is valid using regex
def check_email_format(email_input):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email_input) is not None


# ---------- Function to add a new contact ----------
# This function takes user input and stores
# contact details inside dictionary
# ---------- Function to update existing contact ----------
# This function updates phone, email, address or category
def modify_contact(contact_book, name):

    print(f"\n--- UPDATE CONTACT: {name} ---")

    contact = contact_book[name]

    # Update phone
    new_phone = input("Enter new phone (press Enter to keep old): ").strip()
    if new_phone:
        valid, cleaned = check_phone_number(new_phone)
        if valid:
            contact["phone"] = cleaned
        else:
            print("Invalid phone number. Keeping old one.")

    # Update email
    new_email = input("Enter new email (press Enter to keep old): ").strip()
    if new_email:
        if check_email_format(new_email):
            contact["email"] = new_email
        else:
            print("Invalid email format. Keeping old one.")

    # Update address
    new_address = input("Enter new address (press Enter to keep old): ").strip()
    if new_address:
        contact["address"] = new_address

    # Update category
    new_category = input("Enter new category (press Enter to keep old): ").strip()
    if new_category:
        contact["category"] = new_category

    # Update timestamp
    contact["updated_on"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Contact updated successfully!")



# ---------- Function to search contacts ----------
# This function searches by partial name match
def find_contacts(contact_book, keyword):

    keyword = keyword.lower()
    found_contacts = {}

    for name, details in contact_book.items():
        if keyword in name.lower():
            found_contacts[name] = details

    return found_contacts


# ---------- Function to display search results ----------
# This function prints contacts in clean format
def show_results(results_dict):

    if not results_dict:
        print("No matching contacts found.")
        return

    print("\nSearch Results:")
    print("-" * 40)

    count = 1
    for name, details in results_dict.items():
        print(f"{count}. {name}")
        print(f"   Phone   : {details['phone']}")

        if details["email"]:
            print(f"   Email   : {details['email']}")

        if details["address"]:
            print(f"   Address : {details['address']}")

        print(f"   Category: {details['category']}")
        print("-" * 40)

        count += 1
