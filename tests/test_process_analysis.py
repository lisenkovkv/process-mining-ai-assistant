import unittest
from src.process_analysis import analyze_process

class TestProcessAnalysis(unittest.TestCase):
    def test_analyze_process_valid_log(self):
        log = [{"event": "start", "timestamp": "2024-01-01"}, {"event": "end", "timestamp": "2024-01-02"}]
        result = analyze_process(log)
        self.assertIsNotNone(result)
        self.assertIn('process_model', result)

if __name__ == '__main__':
    unittest.main()