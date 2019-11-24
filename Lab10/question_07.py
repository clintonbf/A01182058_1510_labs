def set_up_food_list() -> dict:
    """
    Set up food list for the user.

    :return: dictionary

    >>> set_up_food_list()
     {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
             "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
    """

    return {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
            "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}


def sum_calories(dic: dict) -> int:
    """
    Sum all the values in a dictionary.

    :param dic: a dictionary
    :precondition: every value in dic is an int
    :precondition: dic is non-empty
    :precondition: dic values > 0
    :postcondition: sum of dic values is calculated and output
    :return: int

    >>> sum_calories({'a': 1, 'b':2})
    3
    """
    return sum(dic.values())


def calculate_average(dic: dict) -> float:
    """
    Calculate average of a list.

    :param dic: dictionary
    :precondition:  every value in dic is an int
    :precondition: dic is non-empty
    :precondition: dic values > 0
    :postcondition: average of dic values is calculated to 1 decimal place
    :return: float

    >>> calculate_average({'a': 1, 'b': 2, 'c': 3})
    2
    >>> calculate_average({'a': 1, 'b': 2, 'c': 55})
    19.3
    """

    return round(sum(dic.values()) / len(dic.values()), 1)


def request_food_item() -> str:
    """
    Get food item from user.

    :postcondition:
    :return: string
    """
    return input("Enter food item to add, or ’q’ to exit: ")
