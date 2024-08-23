import unittest
from src.data_preprocessing import preprocess_data
from src.process_analysis import analyze_process
from src.ai_module import ai_model

class TestIntegration(unittest.TestCase):
    def test_full_pipeline(self):
        input_data = "path_to_valid_input.csv"
        preprocessed_data = preprocess_data(input_data)
        process_model = analyze_process(preprocessed_data)
        predictions = ai_model(preprocessed_data)
        self.assertTrue(predictions)

if __name__ == '__main__':
    unittest.main()