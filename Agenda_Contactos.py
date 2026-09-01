def display_menu():
    print("Contact Book Menu:")
    print("1. Añadir Contacto")
    print("2. Ver Contacto")
    print("3. Editar Contacto")
    print("4. Eliminar Contacto")
    print("5. Ver todos los Contactos")
    print("6. Salir")

def add_contact(contact_book):
    name = input("Nombre del contacto")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    direccion = input("Direccion: ")

    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": telefono,      
            "email": correo,
            "address": direccion
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    name = input("Contacto que desea ver: ")

    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Contacto que desea editar: ")

    if name in contact_book:
        telefono = input("Agregue un nuevo telefono: ")
        correo = input("Agregue un nuevo correo: ")
        direccion = input("Agregue una nueva doreccion: ")

        if telefono != '':
            contact_book[name]["phone"] = telefono  
        if correo != '':
            contact_book[name]["email"] = correo
        if direccion != '':
            contact_book[name]["address"] = direccion
        
        print("Contact updated successfully!")  
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Nombre que desea eliminar: ")

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")

contact_book = {}

while True:
    display_menu()
    opcion = int(input("Ingrese la opcion que mas deseas: "))

    if opcion == 1:
        add_contact(contact_book)
    elif opcion == 2:
        view_contact(contact_book)
    elif opcion == 3:
        edit_contact(contact_book)
    elif opcion == 4:
        delete_contact(contact_book)
    elif opcion == 5:
        list_all_contacts(contact_book)
    elif opcion == 6:
        print("Usted ah salido del sistema.")
        break