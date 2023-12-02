from error_handler import input_error
from errors import ContactExistsError, ContactNotFoundError, IncorrectArgumentsQuantityError, ContactsAreEmptyError


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("To add a new contact use 'add <name> <phone>' command.")
    name, phone = args
    if name in contacts:
        raise ContactExistsError(f"If you want to update the phone number please use add {name} {phone}.")
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IncorrectArgumentsQuantityError("Use 'change <name> <phone>' command for changing contact.")
    name, phone = args
    if name not in contacts:
        raise ContactNotFoundError
    contacts[name] = phone
    return "Contact changed."


@input_error
def get_phone(args, contacts):
    if len(args) != 1:
        raise IncorrectArgumentsQuantityError("To get the user's phone number please use 'phone <name>' command.")
    name = args[0]
    if name not in contacts:
        raise ContactNotFoundError
    return f"{name}'s phone: {contacts[name]}"


def get_all_contacts(contacts):
    items = contacts.items()
    if len(items) == 0:
        raise ContactsAreEmptyError
    return "\n".join([f"{name}'s phone: {phone}" for name, phone in items])
