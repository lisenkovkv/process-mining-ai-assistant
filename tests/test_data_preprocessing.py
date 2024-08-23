import unittest
from src.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data_valid_input(self):
        input_data = "path_to_valid_input.csv"
        result = preprocess_data(input_data)
        # Проверка результата
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, list))

    def test_preprocess_data_invalid_input(self):
        input_data = "invalid_path.csv"
        with self.assertRaises(FileNotFoundError):
            preprocess_data(input_data)

if __name__ == '__main__':
    unittest.main()