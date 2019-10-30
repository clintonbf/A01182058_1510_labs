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
        return batch.insert(0, list_length)
    else:
        return []


def main():
    list_tagger([])


if __name__ == '__main__':
    main()
