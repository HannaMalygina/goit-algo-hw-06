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
        self.set_phone(value)
        
    def validate_phone(phone_str):
        if len(phone_str) != 10 or not phone_str.isdigit():
            raise ValueError(f'Invalid number {phone_str}')

    def set_phone(self, phone_str):
        Phone.validate_phone(phone_str)
        super().__init__(phone_str)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str):
        Phone.validate_phone(phone_str)
        self.phones.append(Phone(phone_str))           

    def edit_phone(self, phone_str, new_phone_str):
        self.find_phone(phone_str).set_phone(new_phone_str)

    def remove_phone(self, phone_str):
        self.phones.remove(self.find_phone(phone_str))
            
    def find_phone(self, phone_str):
        for phone_obj in self.phones:
            if phone_str == phone_obj.value:
                return phone_obj
        raise ValueError(f"Phone number {phone_str} not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record 

    def find(self, name_str):
        return self.data[name_str]

    def delete(self, name_str):
        del self.data[name_str]



# record = Record("john")
# record.add_phone("0123456789")
# print(record)
# record.add_phone("1234567809")
# print(record)
# record.edit_phone("1234567809", "12")
# record.remove_phone("1234567809")
        

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
print(*[record for record in book.data.values()])

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223833")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
