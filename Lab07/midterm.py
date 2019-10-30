import random


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

    list_length = len(batch)

    if list_length > 0:
        batch.insert(0, list_length)

    return batch


def cutoff(a_list, divisor):
    """

    :param a_list:
    :param divisor:
    :return:
    """

    count = 0

    for num in a_list:
        if num % divisor == 0:
            count += 1

    return count

def prepender(str_list, s):
    """

    :param str_list:
    :param s:
    :return:
    """

    for i in range(0, len(str_list)):
        str_list[i] = s + str_list[i]


def name_list():
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
    summation = 0

    for num in range(0, upper_bound):
        if num % 3 == 0:
            summation += num

    return summation


def die_thing():
    die_rolls = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    sides = int(input("how many sides is your die?"))
    rolls = int(input("how many times should I roll?"))

    for i in range(0, rolls):
        roll = random.randint(1, sides)

    die_rolls[roll] += 1

    print("Here's what I rolled:")

    for k, v in die_rolls.items():
        print(str(k), ":", str(v))


def main():


if __name__ == '__main__':
    main()
