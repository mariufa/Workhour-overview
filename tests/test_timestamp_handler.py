import unittest
import os
from time import time
from src.timestamp_handler import TimestampHandler

class TestTimestampHandler(unittest.TestCase):

    def setUp(self):
        self.file_name = "test.txt"
        # Clear the file
        test_file = open(self.file_name, "w")
        test_file.close()

        now = time()
        yesterday = now - 60*60*24
        self.handler = TimestampHandler(self.file_name, now, False)
        self.handler.register_timestamp()
        self.handler.timestamp = yesterday
        self.handler.register_timestamp()

    def test_register_timestamps(self):
        timestamps = self.handler.get_timestamps()
        self.assertEqual(2, len(timestamps))

    def tearDown(self):
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()
