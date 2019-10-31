import random
import doctest


def list_tagger(batch):
    """
    Determine length of a list.
    Prepend list length to the list.

    :param batch: list
    :precondition: batch is a list
    :postcondition: list with length at element 0 created
    :return: list

    >>>list_tagger([])
    [0]
    >>>list_tagger(['a', 'b'])
    [2, 'a', 'b']
    """

    batch.insert(0, len(batch))

    return batch


def cutoff(a_list, divisor):
    """
    Count the number of integers in a list that are a multiple of a number.

    :param a_list: list
    :param divisor: integer
    :precondition: a_list is a list
    :precondition: divisor is an integer
    :precondition: divisor >= 0
    :postcondition: number of integers in the list that are a multiple of divisor
    :return: integer

    >>>cutoff([1, 2, 3, 4, 5, 6, 7, 8], 2)
    4
    >>>cutoff([9, 9, 9, 4], 3)
    3
    >>>cutoff([1], 5)
    0
    """

    count = 0

    for num in a_list:
        if num % divisor == 0:
            count += 1

    return count


def prepender(str_list, s):
    """
    Prepend a string to the beginning of each string in a list.

    :param str_list: list
    :param s: what to prepend, string
    :precondition: str_list is a list
    :precondition: str_list has >0 elements
    :precondition: s is a string
    :postcondition: s is prepended to every string in str_list

    >>>prepender(['bar', 'fighters'], 'foo')
    ['foobar', 'foofighters']
    """

    for i in range(0, len(str_list)):
        str_list[i] = s + str_list[i]


def name_list():
    """
    Create a dictionary of counts of each letter supplied from a list of names.

    :postcondition: dictionary, key = letter, value = tally of the letter in the supplied list
    :return: dictionary
    """
    names = []
    name_dict = {}
    chosen = ""

    while chosen.lower() != "quit":
        chosen = input("Enter a name, or 'quit' to stop")

        if chosen == 'quit':
            pass
        else:
            names.append(chosen)

    for name in names:
        name_dict[len(names)].append(name)

    return name_dict


def multiples_of_3(upper_bound):
    """
    Sum all positive numbers below an upper bound that are multiples of 3.

    :param upper_bound: int
    :precondition: upper_bound > 1
    :postcondition: sum all positive integers below upper_bound that are multiples of 3.
    :return: int

    >>>multiples_of_3(10)
    18
    >>>multiples_of_3(2)
    0
    """
    summation = 0

    for num in range(0, upper_bound):
        if num % 3 == 0:
            summation += num

    return summation


# What are the DJEs here?
def die_thing():
    """
    Roll a die several times and tally the results.

    :postcondition: the number of time that each side is rolled is tallied
    :return: dictionary
    """
    die_rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    sides = int(input("how many sides is your die?"))
    rolls = int(input("how many times should I roll?"))

    for i in range(0, rolls):
        roll = random.randint(1, sides)

        die_rolls[roll] += 1

    print("Here's what I rolled:")

    for k, v in die_rolls.items():
        print(str(k), ":", str(v))


def main():
    pass


if __name__ == '__main__':
    main()
