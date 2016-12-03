import unittest
from time import time
from src.timestamp_handler import Timestamp_handler

class TestTimestampHandler(unittest.TestCase):

    def setUp(self):
        self.file_name = "test.txt"
        # Clear the file
        test_file = open(self.file_name, "w")
        test_file.close()

        now = time()
        self.handler = Timestamp_handler(self.file_name, now, False)

    def test_get_empty_timestamps(self):
        timestamps = self.handler.get_timestamps()
        self.assertEqual([], timestamps)

if __name__ == '__main__':
    unittest.main()
