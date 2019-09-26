import sys


def main():
    print("Div by 0 example: div by..... 0")
    print(1 / 0)

    print("Index error 1: calling an element from string that is 1 higher than the string's length")
    word = "error"
    print(word[5])

    print("Index error 2: calling a command line argument that wasn't provided")
    print(sys.argv[1])

    print("Type error: supplying an int as an argument to print()")
    print("The number is " + 5)


if __name__ == "__main__":
    main()
