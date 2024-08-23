import unittest
from src.ai_module import ai_model

class TestAIModule(unittest.TestCase):
    def test_ai_model_prediction(self):
        event_log = [{"event": "start"}, {"event": "end"}]
        predictions = ai_model(event_log)
        self.assertEqual(len(predictions), len(event_log))
        self.assertIn('prediction', predictions[0])

if __name__ == '__main__':
    unittest.main()