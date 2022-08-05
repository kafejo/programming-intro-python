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
    num = int(input())

    for i in range(num):    # Range method starts from 0 until < x.
        print(i)            # range (3) will give you 0, 1, 2

    # Question: How would you fix it that it prints 1, 2, 3 instead of 0, 1, 2?


if __name__ == "__main__":
    example1()
    #example2()
