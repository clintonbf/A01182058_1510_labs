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
    return sum(list(dic.values()))


def calculate_average(dic: dict) -> float:
    """
    Calculate average of a list.

    :param dic: dictionary
    :precondition:  every value in dic is an int
    :precondition: dic is non-empty
    :precondition: dic values > 0
    :postcondition: average of dic values is calculated to 1 decimal places
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


def old_main():
    pass
    # # Input loop
    # new_item = input("Enter food item to add, or ’q’ to exit: ")
    # while new_item != "q":
    #     new_item_calories = int(input("Enter calories for " + new_item + ": "))
    #     _calories[new_item] = new_item_calories
    #
    #     total_calories = 0
    #     for item in _calories:  # Sum calories for all items
    #         total_calories = total_calories + _calories[item]
    #
    #     food_item_names = []
    #     for item in _calories:
    #         food_item_names.append(item)
    #
    #     avg_calories = total_calories / len(_calories)
    #
    #     print("\nFood Items:", sorted(food_item_names))
    #     print("Total Calories:", total_calories,
    #           "Average Calories: %0.1f\n" % avg_calories)
    #
    #     new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    calories = set_up_food_list()

    new_item = request_food_item()

    while new_item != "q":
        new_item_calories = int(input("How many calories is " + new_item + "?"))
        calories[new_item] = new_item_calories

        print("\nFood Items:", sorted(calories.keys()))

        print("Total calories: ", sum_calories(calories))

        print("Average calories: ", calculate_average(calories))

        new_item = request_food_item()


if __name__ == '__main__':
    main()
