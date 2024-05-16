from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Неправильний формат телефонного номера")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Неправильний формат дня народження. Використовуйте DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Неправильний формат телефонного номера")
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        birthday_str = str(self.birthday.value) if self.birthday else 'Not specified'
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        del self.data[name]

    def find(self, name):
        return self.data.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if days_until_birthday <= 7:
                    if birthday_this_year.weekday() >= 5:  
                        days_until_birthday += 7 - birthday_this_year.weekday()
                        birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())

                    congratulation_date = birthday_this_year.strftime("%Y.%m.%d")
                    upcoming_birthdays.append({"name": record.name.value, "congratulation_date": congratulation_date})

        return upcoming_birthdays
    
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

def parse_input(user_input):
    return user_input.split()

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}"
    else:
        return f"Contact {name} not found"

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return f"{name}'s birthday: {record.birthday.value}"
    else:
        return f"Contact {name} not found"

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"{b['name']}'s birthday is on {b['congratulation_date']}" for b in upcoming_birthdays])
    else:
        return "No upcoming birthdays"

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone number updated for {name}"
    else:
        return f"Contact {name} not found"

@input_error
def phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return f"{name}'s phone numbers: {', '.join(str(p) for p in record.phones)}"
    else:
        return f"Contact {name} not found"

@input_error
def all_contacts(args, book):
    return "\n".join(str(record) for record in book.data.values())

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change(args, book))

        elif command == "phone":
            print(phone(args, book))

        elif command == "all":
            print(all_contacts(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
