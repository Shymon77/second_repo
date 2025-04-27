def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Usage: change [name] [new phone]")
            elif args[0] in contacts:
                contacts[args[0]] = args[1]
                print("Contact updated.")
            else:
                print("Contact not found.")
        elif command == "all":
            if not contacts:
                print("No contacts saved.")
            else:
                print("Saved contacts:")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
