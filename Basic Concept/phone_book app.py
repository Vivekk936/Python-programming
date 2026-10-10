class PhoneBook:
    phone_directory=[]
    def __init__(self,name,phone_number):
        self.name=name
        self.phone=phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}\nContact Number: {self.phone}"

    @classmethod
    def display_contact(cls):
        if len(cls.phone_directory)== 0:
            print("No phone number")

        else:
            for contact in cls.phone_directory:
                print(f"{contact.name}:{contact.phone}")

    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone
        return f"No contact named {search_name}"
    @staticmethod
    def validate_Phone_number(number):
        if len(number)==10 and number.isdigit():
            return True
        else:
            return False


n_contacts=int(input("Enter the number of contacts"))
for i in range (n_contacts):
    name=input("Enter the contact name")
    phone_number=input("Enter the contact phone number")
    if PhoneBook.validate_Phone_number(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid phone number of {name}")

"""
c1= PhoneBook("John",3453535366)
c2= PhoneBook("Alice",3453535336)
#print(PhoneBook.phone_directory)
c3= PhoneBook("Bob",3453535352)

#PhoneBook.display_contact()"""

PhoneBook.display_contact()
print(PhoneBook.search_contact("John"))
print(PhoneBook.search_contact("Bob"))