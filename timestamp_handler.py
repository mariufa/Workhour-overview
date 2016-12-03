from time import time
from datetime import datetime

class Timestamp_handler(object):

    def __init__(self, file_name, timestamp, override_existing_today):
        self.file_name = file_name
        self.timestamp = timestamp
        self.override_existing_today = override_existing_today
        self.number_days_history = 80

    def register_timestamp(self):
        opened_file = open(self.file_name)
        timestamps = opened_file.readLines()
        last_timestamp = float(timestamps[-1])
        if (self.is_same_day(last_timestamp) and self.override_existing_today):
            timestamps[-1] = str(timestamps)
        else:
            if ()
            timestamps.append(self.timestamp)
        save_timestamps

    def is_same_day(self, last_timestamp):
        current_date = datetime.fromtimestamp(self.timestamp).isocalendar()
        last_date = datetime.fromtimestamp(last_timestamp).isocalendar()
        return current_date == last_date
