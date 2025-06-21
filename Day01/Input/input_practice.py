#Input-Driven Mini Program
while True:
    user = input("Type a command (help/exit): ").strip().lower()
    if user == "help":
        print("Available commands: help, exit")
    elif user == "exit":
        print("Goodbye!")
        break
    else:
        print(f"Unknown command: {user}")
