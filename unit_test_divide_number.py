import unittest
from sklearn.linear_model import LinearRegression
import numpy as np

def divide_by_two(number):
    return number / 2

def generate_training_data_divide_by_two(num_samples):
    training_data = []
    for _ in range(num_samples):
        input_value = round(np.random.uniform(-1000, 1000), 3)
        output_value = divide_by_two(input_value)
        training_data.append((input_value, output_value))
    return training_data

def model_AI(training_data):
    X = np.array([item[0] for item in training_data]).reshape(-1, 1)
    y = np.array([item[1] for item in training_data])

    model = LinearRegression()
    model.fit(X, y)
    return model

class TestDivideByTwoWithAI(unittest.TestCase):
    def test_with_ai_generated_cases(self):
        new_data = np.array([0, 8.752, -15.66]).reshape(-1, 1)
        training_data = generate_training_data_divide_by_two(1000)
        model = model_AI(training_data)
        expected_results = model.predict(new_data)

        for i, test_case in enumerate(new_data):
            with self.subTest(test_case=test_case):
                result = divide_by_two(test_case)
                self.assertAlmostEqual(float(result), float(expected_results[i]), places=5)

if __name__ == '__main__':
    unittest.main()
