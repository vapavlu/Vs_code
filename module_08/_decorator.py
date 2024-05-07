def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Enter both name and phone."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(name, contacts):
    return contacts[name]

@input_error
def get_all_contacts(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        command = input("Enter a command: ").strip().split()
        if not command:
            continue
        if command[0] == "add":
            print(add_contact(command[1:], contacts))
        elif command[0] == "phone":
            print(get_phone(command[1], contacts))
        elif command[0] == "all":
            print(get_all_contacts(contacts))
        elif command[0] == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
