from unittest import TestCase

from Lab10.question_07 import set_up_food_list


class TestSet_up_food_list(TestCase):
    def test_set_up_food_list(self):
        expected_dict = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                         "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

        self.assertEqual(set_up_food_list(), expected_dict)
