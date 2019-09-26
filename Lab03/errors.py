import sys


def display_div_error():
    print("Div by 0 example")
    print(1 / 0)


def display_index_error_1():
    print("Index error 1")
    word = "error"
    print(word[5])


def display_index_error_2():
    print("Index error 2")
    print(sys.argv[1])


def display_type_error():
    print("Type error")
    print("The number is " + 5)


def main():
    display_div_error()
    # display_index_error_1()
    # display_index_error_2()
    # display_type_error()


if __name__ == "__main__":
    main()
