def contact_book():
    print("---CONTACT BOOK---")
    contacts = {}
    
    while True:
        print("press '1' to ADD NEW CONTACT")
        print("press '2' to DELETE A CONTACT")
        print("press '3' to VIEW CONTACT INFORMATION")
        print("press '4' to SEARCH A CONTACT")
        print("press '5' to UPDATE A CONTACT")
        print("press '6' to EXIT")
        
        choice = input("Enter your choice from 1/2/3/4/5/6: ")

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid output, please choose a correct option from 1 to 6")
            continue

        if choice == '1':
            name = input("Enter the name of the contact: ")
            if not name.isalpha():
                print("Invalid name. Please enter a valid name.")
                continue
            
            phone = input("Enter the phone number of the contact: ")
            if not phone.isdigit() or len(phone) != 10:
                print("Invalid phone number. Please enter a 10-digit number.")
                continue
            email = input("Enter the email of the contact: ")
            if '@' not in email:
                print("Invalid email address.")
                continue
            address = input("Enter the address of the contact: ")
            
            if not name or not phone or not email or not address:
                print("All fields are required.")
                continue
            
            if name in contacts:
                print(f"The contact {name} already exists in the contact book.")
            else:
                contacts[name] = {'phone': phone, 'email': email, 'address': address}
                print(f"The contact {name} has been added successfully.")

        elif choice == '2':
            name = input("Enter the name of the contact you want to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"The contact {name} has been removed from the contact book.")
            else:
                print(f"The contact {name} is not in the contact book.")

        elif choice == '3':
            if not contacts:
                print("No contacts to display.")
            else:
                print("Contacts:")
                for name, info in contacts.items():
                    print(f"{name}: Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

        elif choice == '4':
            name = input("Enter the name of the contact you want to search: ")
            if name  in contacts:
                info = contacts[name]
                print(f"Contact found: {name}")
                print(f"{name}: Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            else:
                print(f"The contact {name} is not in the contact book.")

        elif choice == '5':
            name = input("Enter the name of the contact you want to update: ")
            if name in contacts:
                print(f"Updating contact: {name}")
                new_phone = input("Enter the new phone number: ")
                new_email = input("Enter the new email: ")
                new_address = input("Enter the new address: ")
                
                contacts[name] = {'phone': new_phone, 'email': new_email, 'address': new_address}
                print(f"The contact {name} has been updated successfully.")
            else:
                print(f"The contact {name} is not in the contact book.")

        elif choice == '6':
            print("Exiting the contact book.thankyou for using CODSOFT CONTACTBOOK!!")
            break

contact_book()
# This code implements a simple contact book application with options to add, delete, view, search, and update contacts.