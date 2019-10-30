import doctest


def sparse_add(sparse_1, sparse_2):
    """
    Add 2 sparse vectors.

    :param sparse_1: sparse vector
    :param sparse_2: sparse vector
    :precondition: sparse_1 contains integers
    :precondition: sparse_2 contains integers
    :postcondition: sparse_1 and sparse_2 are summed
    :return: dictionary

    >>> sparse_add({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})
    {1: 2, 2: 4, 3: 6}
    >>> sparse_add({}, {1: 1, 2: 2, 3: 3})
    {1: 1, 2: 2, 3: 3}
    """

    return_dictionary = {}
    found_keys = {}

    for elem in sparse_1.keys():
        addition = 0

        if elem in sparse_2:
            found_keys[elem] = 1
            addition = sparse_2[elem]  # An addition value will save us a couple lines

            if sparse_1[elem] + addition == 0:
                pass
            else:
                return_dictionary[elem] = sparse_1[elem] + addition
        else:
            return_dictionary[elem] = sparse_1[elem] + addition

    for elem in sparse_2.keys():
        if elem in found_keys:
            pass  # this key was found in the check with sparse_1
        else:
            return_dictionary[elem] = sparse_2[elem]

    return return_dictionary


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
