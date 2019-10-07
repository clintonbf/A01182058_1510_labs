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
    :precondition: number_of_rolls [1, 3]
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
