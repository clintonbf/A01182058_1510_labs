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


def did_user_hit_a_wall(direction: str, character: dict) -> bool:
    """
    Determine if user hit a wall when moving.

    :param direction: string
    :param character: dictionary
    :precondition: direction is a single character in [n, s, w, e]
    :precondition: character is a dictionary
    :precondition: character contains key "x-coord"
    :precondition: character contains key "y-coord"
    :precondition: -1 > x-coord < 5
    :precondition: -1 > y-coord < 5
    :postcondition: determine whether valid movement direction ran into a wall
    :return: bool

    >>>did_user_hit_a_wall(n, {'x-coord': 0, 'y-coord': 3})
    False
    >>>did_user_hit_a_wall(n, {'x-coord': 0, 'y-coord': 0})
    True
    >>>did_user_hit_a_wall(e, {'x-coord': 4, 'y-coord': 3})
    True
    >>>did_user_hit_a_wall(e, {'x-coord': 0, 'y-coord': 3})
    False
    """

    if direction == 'n':
        if character['y-coord'] == 0:
            return True
        else:
            return False
    elif direction == 's':
        if character['y-coord'] == 4:
            return True
        else:
            return False
    elif direction == 'e':
        if character['x-coord'] == 4:
            return True
        else:
            return False
    elif direction == 'w':
        if character['x-coord'] == 0:
            return True
        else:
            return False


def advise_of_movement_error(error: int):
    """
    Notify user they made an invalid movement.

    :param error: int
    :precondition: error is 1 if invalid movement option was provided
    :precondition: error is 2 if user hit a wall
    :postcondition: a helpful message is produced

    >>>advise_of_movement_error(1)
    "Invalid movement option. Please enter again (n, s, w, e)"
    >>>advise_of_movement_error(2)
    "You hit a wall; ouch. Try a different direction(n, s, w, e)"
    """

    if error == 1:
        print("Invalid movement option. Please enter again (n, s, w, e)")
    elif error == 2:
        print("You hit a wall; ouch. Try a different direction(n, s, w, e)")


def move_char(direction: str, character: dict):
    """
    Move the character to a new location.

    :param character: dictionary
    :param direction: string
    :precondition: direction is a single character in [n, s, w, e]
    :precondition: character is a dictionary
    :precondition: character contains key "x-coord"
    :precondition: character contains key "y-coord"
    :precondition: -1 > x-coord < 5
    :precondition: -1 > y-coord < 5
    :postcondition: updates character's position

    >>>move_char('s',  {'x-coord': 0, 'y-coord': 0})
    {'x-coord':0, 'y-coord': 1}
    >>>move_char('e', {'x-coord': 0, 'y-coord': 3})
    {'x-coord':1, 'y-coord': 3}
    """

    if direction == 'n':
        character['y-coord'] -= 1
    elif direction == 's':
        character['y-coord'] += 1
    elif direction == 'e':
        character['x-coord'] += 1
    elif direction == 'w':
        character['x-coord'] -= 1


def reached_end(character: dict) -> bool:
    """
    Check if player is still in maze.

    :param character: dictionary
    :precondition: direction is a single character in [n, s, w, e]
    :precondition: character is a dictionary
    :precondition: character contains key "x-coord"
    :precondition: character contains key "y-coord"
    :precondition: -1 > x-coord < 5
    :precondition: -1 > y-coord < 5
    :postcondition: determines if this nightmare has ended
    :return: bool

    >>>reached_end({'x-coord': 0, 'y-coord': 3})
    True
    >>>reached_end({'x-coord': 4, 'y-coord': 4})
    False
    """

    if character['x-coord'] == 4 and character['y-coord'] == 4:
        return True
    else:
        return False


def game():
    kafka_box = create_board()
    rat = create_character()

    still_in_box = True

    while still_in_box:
        movement = get_movement()

        while not validate_movement(movement):
            advise_of_movement_error(1)
            movement = get_movement()

        if did_user_hit_a_wall(movement, rat):
            still_in_box = True
            advise_of_movement_error(2)
        else:
            move_char(movement, rat)
            print("You're now at (" + str(rat['x-coord']) + "," + str(rat['y-coord']) + ")")

            if reached_end(rat):
                still_in_box = False

    print("You have escaped! Have some cheese.")


def main():
    game()


if __name__ == '__main__':
    main()
