"""
Control flow, boolean
"""


def main():
    print("What age are you?")
    age = int(input())      # Ask for input and re-type it into integer

    is_adult = age >= 18    # Boolean value can be either `true` or `false`

    if is_adult:
        print("You can drink alcohol!")
    else:
        print("You cannot drink alcohol.")

    print("Are you married?")

    married = input()

    if married == "yes":
        print("Cool. What is your wife name?")
        wife_name = input()
        print(f"Say hi to your wife {wife_name}")
    elif married == "no":
        print("You will be one day.")
    else:
        print("That's not an acceptable answer.")


if __name__ == "__main__":
    main()

