import random


def single_roll(number_of_sides):
    """
    Execute a single die roll.

    :param number_of_sides: int
    :precondition: number_of_sides > 0
    :postcondition: a random integer [1, number_of_sides]
    :return: int
    """

    return random.randint(1, number_of_sides)


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate sum of  die rolls.

    :param number_of_rolls: int
    :param number_of_sides: int
    :precondition: number_of_rolls > 0 < 4
    :precondition: number_of_sides > 0
    :postcondition: calculate the sum of all the rolls
    :return: int
    """

    invalid_arg = False
    roll_sum = 0

    # Check both arguments, either one of them being 0 should return a 0
    if number_of_rolls == 0:
        invalid_arg = True

    if number_of_sides == 0:
        invalid_arg = True

    # If both arguments are > 0, roll and sum
    if invalid_arg:
        roll_sum = 0
    else:
        roll_sum = single_roll(number_of_sides)  # Since we know there's at least 1 roll, no need to enclose in an "if"
        number_of_sides = number_of_sides - 1

        # Rules are < 4 rolls, so subtraction will suffice to manage the iteration-size
        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

    return roll_sum


def pick_letter():
    """
    Generate a random lowercase letter.

    :postcondition: a single, lowercase letter generated
    :return: string
    """

    # [97 - 122] = [a - z]
    return chr(random.randint(97, 122))


def create_name(length):
    """
    Concatenate randomly generated letters.

    :param length: int
    :precondition: length is integer
    :precondition: 0 < length < 6
    :postcondition: a string of letters, length characters long
    :return: string
    """

    return_value = ""

    if length < 0:
        return_value = None
    else:
        return_value = pick_letter()
        length = length - 1

        if length:
            return_value = return_value + pick_letter()
            length = length - 1  # We can use subtractions to mimic iterative behaviour, since length < 6

        if length:
            return_value = return_value + pick_letter()
            length = length - 1

        if length:
            return_value = return_value + pick_letter()
            length = length - 1

        if length:
            return_value = return_value + pick_letter()
            length = length - 1

        return_value = return_value.title()

    return return_value


def main():
    print("Test: 3, 6")
    print(str(roll_die(3, 6)))
    print("Test: 0, 5")
    print(str(roll_die(0, 5)))
    print("Test: 3, 0")
    print(str(roll_die(3, 0)))
    print("Test: 0, 0")
    print(str(roll_die(0, 0)))

    print("###############################")
    print("Testing create_name()")
    print("###############################")

    print("Test, 4: '" + create_name(4) + "'")
    print("Test, 2: '" + create_name(2) + "'")
    print("Test, 5: '" + create_name(5) + "'")
    print("Test, 6: '" + create_name(-1) + "'")  # This will throw a runtime exception


if __name__ == "__main__":
    main()

