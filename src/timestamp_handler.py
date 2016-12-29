from time import time
from datetime import datetime

REGISTER_START_FILE_NAME = "workhour_start.txt"
REGISTER_END_FILE_NAME = "workhour_end.txt"

class TimestampHandler(object):
    """
    Handler to save a timestamp to a file. Either append or replace timestamps from same day
    """

    def __init__(self, file_name, timestamp, override_existing_today):
        self.file_name = file_name
        self.timestamp = timestamp
        self.override_existing_today = override_existing_today
        self.NUMBER_DAYS_HISTORY = 80

    def register_timestamp(self):
        timestamps = get_timestamps(self.file_name)
        last_timestamp = self.get_last_timestamp(timestamps)
        timestamps = self.update_timestamps(last_timestamp, timestamps)
        self.save_timestamps(timestamps)

    def get_last_timestamp(self, timestamps):
        if (len(timestamps) == 0):
            return -1
        else:
            return float(timestamps[-1])

    def update_timestamps(self, last_timestamp,  timestamps):
        if (is_same_day(self.timestamp, last_timestamp) and self.override_existing_today):
            timestamps[-1] = str(self.timestamp)
        elif not is_same_day(self.timestamp, last_timestamp):
            timestamps.append(self.timestamp)
            if (len(timestamps) > self.NUMBER_DAYS_HISTORY):
                timstamps.pop(0)
        return timestamps

    def save_timestamps(self, timestamps):
        opened_file = open(self.file_name, 'w')
        for stamp in timestamps:
            opened_file.write("%s\n" % stamp)
        opened_file.close()

def is_same_day(stamp_one, stamp_two):
    if stamp_one == -1 or stamp_two == -1:
        return False
    date_one = datetime.fromtimestamp(stamp_one).isocalendar()
    date_two = datetime.fromtimestamp(stamp_two).isocalendar()
    return date_one == date_two

def get_timestamps(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()
