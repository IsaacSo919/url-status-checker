import unittest
from checker import describe_status_code


class TestStatusDescription(unittest.TestCase):
    def test_404_description(self):
        result = describe_status_code(404)
        self.assertEqual(
            result,
            "Not Found: The requested resource could not be found."
        )
    def test_418_description(self):
        result = describe_status_code(418)
        self.assertEqual(result,"Status code 418: No description available.")
        
        
        


if __name__ == "__main__":
    unittest.main()