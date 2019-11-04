def create_board() -> list:
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


def create_character() -> dict:
    """
    Create a player.

    :postcondition: a player at position (0,0) of the dungeon is created
    :return: dictionary

    >>> create_character()
    {'x-coord': 0, 'y-coord': 0}
    """

    return {'x-coord': 0, 'y-coord': 0}


def get_movement() -> str:
    """
    Get movement direction from user.

    :postcondition: movement direction obtained
    :return: string
    """

    return input("Which direction do you want to go (n, s, e, w)?")


def validate_movement(direction: str) -> bool:
    """
    Validate users movement choice.

    :param direction: string
    :precondition: direction in [n, s, w, e]
    :return: bool

    >>>validate_movement('n')
    True
    >>>validate_movement(1)
    False
    >>>validate_movement('north')
    False
    >>>validate_movement('g')
    False
    """

    if direction.lower() in ['n', 's', 'e', 'w']:
        return True
    else:
        return False


def move_char(direction: int):
    pass


def game():
    create_board()


def main():
    # game()
    print(create_character())


if __name__ == '__main__':
    main()
