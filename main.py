contact_book = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Please try again."

    return wrapper


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contact_book[name] = phone
    return f"Contact {name} added with phone number {phone}"


@input_error
def change_phone(command):
    _, name, phone = command.split()
    if name in contact_book:
        contact_book[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        raise KeyError


@input_error
def get_phone(command):
    _, name = command.split()
    if name in contact_book:
        return f"The phone number for {name} is {contact_book[name]}"
    else:
        raise KeyError


def show_all_contacts():
    if contact_book:
        return "\n".join([f"{name}: {phone}" for name, phone in contact_book.items()])
    else:
        return "The contact book is empty."


def main():
    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            print(add_contact(user_input))
        elif user_input.startswith("change"):
            print(change_phone(user_input))
        elif user_input.startswith("phone"):
            print(get_phone(user_input))
        elif user_input == "show all":
            print(show_all_contacts())
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()