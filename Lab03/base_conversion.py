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