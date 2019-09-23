def calculate_digit (num, base):
    """
    Calculate a digit in a decimal-to-base-n conversion.

    :param num: int, number to convert
    :param base: int, the new base
    :precondition: both arguments are positive integers, base != 10
    :postcondition: conversion to new base
    :return: int
    """
    return num % base


def calculate_divisor (num, base):
    """
    Calculate the divisor in a decimal-to-base-n conversion.

    :param num: int, starting number
    :param base: the new base
    :precondition: both arguments are positive integers, base != 10
    :postcondition: divisor for the next conversion calculation
    :return: int
    """

    return num // base


def combine_digits (num1, num2, num3, num4):
    """
    Concatenate supplied arguments in reverse order.

    :param num1: int
    :param num2: int
    :param num3: int
    :param num4: int
    :precondition: all arguments are positive integers
    :precondition: arguments are supplied in the reverse-order (ie. num1 is the right-most digit)
    :postcondition: string-concatenation of the arguments
    :return: string
    """

    return str(num4) + str(num3) + str(num2) + str(num1)


def base_conversion():
    """
    Convert decimal input into a user-specified base.

    :postcondition: print the converted value to standard output.
    """

    """ In order to convert a decimal integer (x) to base-n (n), we go through iterations:
        Iteration 1: Divide x by n (divide the number by the new base)
            - the remainder is the final digit in the conversion
            - the quotient becomes x for the next iteration (x2)
        
        Iteration 2: Divide x2 by n
            - the remainder is the penultimate digit in the conversion
            - the quotient becomes x for the next iteration (x3)
            
        Iteration 3: divide x3 by n
            - the remainder is the third-last digit in the conversion
            - the quotient becomes x for the next iteration (x4)
    """
    dest_base = int(input("Enter your destination base (between 1 - 9. Note: it all will be belong to us): "))
    max_dec_size = (dest_base ** 4) - 1

    print("The highest decimal number of the dest_base is " + str(max_dec_size))
    num_to_convert = int(input("So, give me a number that is less than " + str(max_dec_size) + ": "))

    # start by dividing num_to_convert by dest_base
    rem_1 = calculate_digit(num_to_convert, dest_base)  # this will be the right-most digit in the conversion
    quo_1 = calculate_divisor(num_to_convert, dest_base)

    #  for the next digit, divide the quotient from the first division by dest_base (etc, etc)
    rem_2 = calculate_digit(quo_1, dest_base)
    quo_2 = calculate_divisor(quo_1, dest_base)

    rem_3 = calculate_digit(quo_2, dest_base)
    quo_3 = calculate_divisor(quo_2, dest_base)

    rem_4 = calculate_digit(quo_3, dest_base)
    #  quo_4 not taken because it's not needed, as per input restriction

    output_str = str(combine_digits(rem_1, rem_2, rem_3, rem_4))
    output_int = int(output_str)

    print("Final result: '" + str(output_int) + "'")


def main():
    base_conversion()


if __name__ == "__main__":
    main()