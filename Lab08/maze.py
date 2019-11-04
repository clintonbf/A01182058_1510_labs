def create_board():
    """
    Create a 5 x 5 game board

    :postcondition: a 5 x 5 game board is created
    :return: list

    >>>create_board()
    [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    """

    game_board = []

    for x_value in range(5):
        row = []
        for y_value in range(5):
            row.append(y_value)

        game_board.append(row)

    return game_board


def create_character():
    """
    Create a player.

    :postcondition: a player at position (0,0) of the dungeon is created
    :return: dictionary

    >>> create_character()
    {'x-cord': 0, 'y-cord': 0}
    """

    return {'x-cord': 0, 'y-cord': 0}


def get_movement():
    pass


def validate_movement():
    pass


def move_char():
    pass


def game():
    create_board()


def main():
    # game()
    print(create_character())


if __name__ == '__main__':
    main()
