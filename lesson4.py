"""
Data structures: Arrays
"""


def main():
    # Declare an array
    fruits = ["Apple", "Banana", "Peach", "Jackfruit"]

    # Iterate over the array items
    for item in fruits:
        print(item)

    # Add new item to the array
    fruits.append("Blueberry")

    # Remove an item
    fruits.remove("Apple")

    # Get how many items is in the array
    count = len(fruits)
    print(f"There are {count} fruits in the array")

    # Check if array contains an item
    if "Banana" in fruits:
        print("Banana is in fruits")
    else:
        print("Banana is not in fruits")

    # Iterate over array with indexes using `enumerate()` function
    for index, value in enumerate(fruits):
        print(f"{index}: {value}")

    # Directly access items by index (starts from zero)
    first_item = fruits[0]
    print(first_item)

    # Directly replace item on specific index
    fruits[0] = "Lemon"     # Replaces Banana with Lemon
    print(fruits)


if __name__ == "__main__":
    main()

