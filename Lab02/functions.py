"""A set of functions for COMP 1510, lab 2."""


def format_name(first_name, last_name):
    """Remove whitespace.

    :param: first_name, a string
    :param: last_name, a string
    :precondition: all arguments are strings
    :postcondition: remove leading and trailing whitespace
    :postcondition: capitalize the first letter of each argument (lowercase the remaining)
    :postcondition: concatenate arguments
    :return: string
    """
    trim_name = first_name.strip()
    trim_surname = last_name.strip()

    return_string = trim_name.title() + " " + trim_surname.title()

    return return_string


def tripler(var):
    """Concatenate supplied argument 3 times.

    :param: var, an int, float, or string
    :precondition: var must be an int, float, or string
    :postcondition: twice-concatenated argument, for a total of 3 iterations.
    :return: string
    """
    return_string = str(var) * 3

    return return_string


def this_year():
    """Impress Chris by calculating the current year using the most phenomenal of computational facts.

    :postcondition: inform the user of a groovy mathematical operation and output the result of said operation.
    :return: int
    """
    #  Katheleen Booth's year of birth
    k_b_yob = 1922
    #  Grace Hopper's year of death
    g_h_yod = 1992
    #  Publishing year of an article by John von Neumann, about.... I forget and didn't bother consulting the internet
    j_v_n_article_year = 1949

    crazy_expression = g_h_yod - k_b_yob + j_v_n_article_year

    return crazy_expression


def base_conversion():
    """Convert decimal input into a user-specified base.

    :postcondition: print the converted value to standard output.
    """
    dest_base = int(input("Enter your destination base (between 1 - 9. Note: it all will be belong to us): "))
    max_dec_size = (dest_base ** 4) - 1

    print("The highest decimal number of the dest_base is " + str(max_dec_size))
    num_to_convert = int(input("So, give me a number that is less than " + str(max_dec_size) + ": "))

    # start by dividing num_to_convert by dest_base
    rem_1 = num_to_convert % dest_base  # this will be the final digit in the conversion
    quo_1 = num_to_convert // dest_base

    #  for the next digit, divide the quotient from the first division by dest_base (etc, etc)
    rem_2 = quo_1 % dest_base
    quo_2 = quo_1 // dest_base

    rem_3 = quo_2 % dest_base
    quo_3 = quo_2 // dest_base

    rem_4 = quo_3 % dest_base
    #  quo_4 not taken because it's not needed, as per lab instructions

    output_str = str(rem_4) + str(rem_3) + str(rem_2) + str(rem_1)
    output_int = str(output_str)

    print("Final result: '" + str(output_int) + "'")


def main():
    #  Demonstration of your_name()
    print("Test (your_name()) #1")
    print("'" + format_name("Clinton", "Fernandes") + "'")

    print("Test (your_name() #2")
    print("'" + format_name("CLINTON", "FERNANDES") + "'")

    print("Test (your_name() #3")
    print("'" + format_name("    CLINTON", "    FERNANDES      ") + "'")

    print("..... moving along......")

    # Demonstration of tripler
    print("Test (tripler() #1")
    print("'" + tripler(3) + "'")

    print("Test (tripler() #2")
    print("'" + tripler("Boo") + "'")

    print("Test (tripler() #3")
    print("'" + tripler(88.88) + "'")

    print(".... continuing.....")

    #  Demonstration of the this_year()
    print("Fun fact: if we take the year of death of Rear Adr. Grace Hopper, \n"
          "subtract the year of birth of Katheen Booth,\n"
          "and then add the year that John von Neumann published his paper on\n"
          "the self-replicating computer program, \n"
          "you get: '" + str(this_year()) + "'!")

    print("....and, finally....")

    #  Demonstration of base_conversion()
    base_conversion()

    print("\nVIOLA\n")
    print("En taro Adun!")
    print("En taro Tassadar!")


if __name__ == "__main__":
    main()

