contacts = {}
 
 
def add_cont():
   name = input("Enter the name of the contact: ")
   number = input("Enter the phone number of the contact: ")
   contacts[name] = number 
   print(f"Contact {name} added successfully.")
 
def search_cont():
   name = input("Enter the name of the contact to search: ")
   if name in contacts: 
       print(f"Contact {name} found. /n Phone number: {contacts[name]}")
   else:
       print(f"Contact {name} not found.")
 
 
def edit_cont():
   name = input("Enter the name of the contact to edit: ")
   if name in contacts: 
       number = input("Enter the new phone number of the contact: ")
       contacts[name] = number 
       print(f"Contact {name} updated successfully.")
   else:
       print(f"Contact {name} not found.")
 
 
def delete_cont():
   name = input("Enter the name of the contact to delete: ")
   if name in contacts: 
       contacts.pop(name)
       print(f"Contact {name} deleted successfully.")
   else:
       print(f"Contact {name} not found.")
 
 
while True:
 
   print("Please choose an option:")
   print("1. Add a new contact")
   print("2. Search for an existing contact")
   print("3. Edit an existing contact")
   print("4. Delete a contact")
   print("5. Exit the program")
 
 
   choice = input("Enter your choice (1-5): ")
 
  
   if choice == "1":
       add_cont()
   elif choice == "2":
       search_cont()
   elif choice == "3":
       edit_contact()
   elif choice == "4":
       delete_contact()
   elif choice == "5":
       print("Thank you for using this program. Goodbye!")
       break 
   else:
       print("Invalid choice. Please try again.")