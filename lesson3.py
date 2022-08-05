"""
Loops
"""


def example1():
    print("Example1: To which number should I count?")
    num = int(input())

    index = 0

    while index != num:     # Repeat this block of code until the condition is false
        index = index + 1
        print(index)


def example2():
    print("Example2: To which number should I count?")
    start = 1
    end = int(input())
    step = 1

    for i in range(start, end, step):    # Range method counts until 'i < end'.
        print(i)            # range (3) will give you 0, 1, 2

    # Question: How would you change it to include the ending number?


if __name__ == "__main__":
    example1()
    #example2()
