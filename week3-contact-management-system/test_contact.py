# ==========================================
# Test File for Contact Management System
# ==========================================

from datetime import datetime

# Sample contacts dictionary for testing
contacts = {
    "Rohan Sharma": {
        "phone": "9876543210",
        "email": "rohan@email.com",
        "address": "Delhi",
        "category": "Friends",
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    "Anjali Mehta": {
        "phone": "9123456780",
        "email": "anjali@email.com",
        "address": "Mumbai",
        "category": "Work",
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}

# ---------- Test: Display All Contacts ----------
print("=== ALL CONTACTS ===")
for name, details in contacts.items():
    print(f"\nName: {name}")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    print(f"Address: {details['address']}")
    print(f"Category: {details['category']}")

# ---------- Test: Search Contact ----------
print("\n=== SEARCH TEST ===")
search_keyword = "Rohan"

found = {}
for name, details in contacts.items():
    if search_keyword.lower() in name.lower():
        found[name] = details

if found:
    print(f"Search results for '{search_keyword}':")
    for name in found:
        print("Found:", name)
else:
    print("No contact found.")

# ---------- Test: Add New Contact ----------
print("\n=== ADD CONTACT TEST ===")
contacts["Priya Singh"] = {
    "phone": "9988776655",
    "email": "priya@email.com",
    "address": "Pune",
    "category": "Family",
    "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "updated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print("New contact added: Priya Singh")

# ---------- Final Contact List ----------
print("\n=== FINAL CONTACT LIST ===")
for name in contacts:
    print(name)
