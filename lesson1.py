"""
Variables and I/O functions
"""


def main():
    print("Hi! What is your first name?")   # Print anything to the user
    name = input()                          # Ask user for input
    print("Thanks. What age are you?")
    age = int(input())                      # Type `int` vs `str`
    next_year_age = age + 1                 # Use + operator to add up two numbers
    print(f"Thanks {name}. Next year you will be {next_year_age} years old.")


if __name__ == "__main__":
    main()

