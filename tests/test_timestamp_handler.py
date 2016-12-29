import unittest
import os
from time import time
from src.timestamp_handler import *

class TestTimestampHandler(unittest.TestCase):

    def setUp(self):
        self.file_name = "test.txt"
        clearFile(self.file_name)

        now = time()
        yesterday = now - 60*60*24
        self.handler = TimestampHandler(self.file_name, now, False)
        self.handler.register_timestamp()
        self.handler.timestamp = yesterday
        self.handler.register_timestamp()

    def test_register_timestamps(self):
        timestamps = get_timestamps(self.file_name)
        self.assertEqual(2, len(timestamps))

    def tearDown(self):
        os.remove(self.file_name)



class TestTimestampHandlerOverrideToday(unittest.TestCase):

    def setUp(self):
        self.file_name = "test2.txt"
        clearFile(self.file_name)

        self.now = time()
        self.one_hour_earlier = self.now - 60*60
        self.yesterday = self.now - 60*60*24
        self.handler = TimestampHandler(self.file_name, self.yesterday, True)
        self.handler.register_timestamp()
        self.handler.timestamp = self.one_hour_earlier
        self.handler.register_timestamp()
        self.handler.timestamp = self.now
        self.handler.register_timestamp()

    def test_register_timestamps_number(self):
        timestamps = get_timestamps(self.file_name)
        self.assertEqual(2, len(timestamps))

    def test_register_timestamps_stamps(self):
        timestamps = get_timestamps(self.file_name)
        self.assertEqual(float(timestamps[0]), self.yesterday)
        self.assertEqual(float(timestamps[1]), self.now)

    def tearDown(self):
        os.remove(self.file_name)

def clearFile(file_name):
    file_to_clear = open(file_name, "w")
    file_to_clear.close()

if __name__ == '__main__':
    unittest.main()
