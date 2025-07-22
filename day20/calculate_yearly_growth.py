# Daily Compound Growth Calculator
# Calculates the result of raising a number to the power of 365

def calculate_yearly_growth():
    while True:
        user_input = input("Enter the daily growth factor (e.g., 1.01) or 'q' to quit: ").strip().lower()

        if user_input == 'q':
            print("Program exited.")
            break

        try:
            number = float(user_input)
            result = number ** 365
            print(f"Result after 365 days: {result}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.\n")


if __name__ == "__main__":
    print("=== Daily Compound Growth Calculator ===")
    calculate_yearly_growth()
