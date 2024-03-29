from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone(value): print ("wrong phone format. Must contain 10 digits")
	
    def validate_phone(self, phone):
        if len(phone) == 10: return True
        else: return False

    def set_phone(self, phone):
        if self.validate_phone(phone): self.value = phone
        else: print ("wrong phone format. Must contain 10 digits")
	
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str):
        phone_obj = Phone(phone_str)
        self.phones.append(phone_obj)           

    def edit_phone(self, phone_str, new_phone_str):
        self.find_phone(phone_str).set_phone(new_phone_str)

    def remove_phone(self, phone_str):
        try:
            self.phones.remove(self.find_phone(phone_str))
        except ValueError:
            pass
            
    def find_phone(self, phone_str):
        for phone_obj in self.phones:
            if phone_str == phone_obj.value: return phone_obj
        message = f'Phone number {phone_str} not found'
        print(message)
        raise ValueError(message)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record 

    def find(self, name_str):
        if self.data.get(name_str):
            return self.data.get(name_str)
        else:
            message = f"Name {name_str} is not in the address book"
            print(message)
            raise ValueError(message)

    def delete(self, name_str):
        try:
            self.find(name_str)
        except ValueError:
            return
        del self.data[name_str]



record = Record("john")
record.add_phone("0123456789")
record.add_phone("1234567809")
record.edit_phone("1234567809", "12")
        

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
