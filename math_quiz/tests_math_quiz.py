import unittest
from math_quiz import function_Random, function_Operation, function_Result


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_Random(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        input = input("Choose Operator into +,-,* : ")
        self.assertTrue(if input = + or input = - or input = *)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (10, 1, '-', '10 - 1', 9),
                (7, 4, '*', '7 * 4', 28)
                ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                 if operator == '+': 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 + num2
                elif operator == '-': 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 - num2
                else: 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 * num2
                self.assertTrue(if actual_problem == expected_problem and actual_answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
