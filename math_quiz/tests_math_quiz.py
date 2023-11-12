import unittest
from math_quiz import get_random_int, get_operator, get_task_with_solution


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operator(self):
        # test if the operator is one of the allowed operators (+, -, *)
        for _ in range(1000):
            operator = get_operator()
            self.assertTrue(operator in ['+', '-', '*'])

    def test_get_task_with_solution(self):
        # test for several math tasks whether the problem statement and the finally calculated result are correct
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 2, '-', '3 - 2', 1),
            (6, 3, '+', '6 + 3', 9),
            (1, 5, '*', '1 * 5', 5),
            (1, 3, '+', '1 + 3', 4),
            (6, 2, '-', '6 - 2', 4),
            (8, 6, '*', '8 * 6', 48),
            (2, 4, '+', '2 + 4', 6),
            (5, 1, '-', '5 - 1', 4),
            (2, 2, '*', '2 * 2', 4)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            (problem_statement, result) = get_task_with_solution(num1, num2, operator)
            self.assertTrue((expected_problem, expected_answer) == (problem_statement, result))

if __name__ == "__main__":
    unittest.main()
