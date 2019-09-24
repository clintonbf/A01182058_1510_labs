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
    Sum all performed die rolls.

    :param number_of_rolls: int
    :param number_of_sides: int
    :precondition: number_of_rolls > 0 < 4
    :precondition: number_of_sides > 0
    :postcondition: calculate the sum of all the rolls
    :return: int
    """

    invalid_arg = False
    roll_sum = 0

    if number_of_rolls == 0:
        invalid_arg = True

    if number_of_sides == 0:
        invalid_arg = True

    if invalid_arg:
        roll_sum = 0
    else:
        roll_sum = single_roll(number_of_sides)  # Since we know there's at least 1 roll, no need to enclose in an "if"
        number_of_sides = number_of_sides - 1

        # Rules are < 4 rolls, so subtraction will manage the iteration-size
        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

    return roll_sum


def main():
    print("Test: 3, 6")
    print(str(roll_die(3, 6)))
    print("Test: 0, 5")
    print(str(roll_die(0, 5)))
    print("Test: 3, 0")
    print(str(roll_die(3, 0)))
    print("Test: 0, 0")
    print(str(roll_die(0, 0)))


if __name__ == "__main__":
    main()

