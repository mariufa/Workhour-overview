from time import time
from datetime import datetime

class Timestamp_handler(object):

    def __init__(self, file_name, timestamp, override_existing_today):
        self.file_name = file_name
        self.timestamp = timestamp
        self.override_existing_today = override_existing_today
        self.NUMBER_DAYS_HISTORY = 80

    def register_timestamp(self):
        timestamps = self.get_timestamps()
        last_timestamp = self.get_last_timestamp(timestamps)




        self.save_timestamps(timestamps)

    def get_timestamps(self):
        opened_file = open(self.file_name, 'r')
        timestamps = opened_file.readlines()
        opened_file.close()
        return timestamps

    def get_last_timestamp(self, timestamps):
        if (len(timestamps) == 0):
            return -1
        else:
            return float(timestamps[-1])

    def update_timestamps(self, timestamps):
        if (self.is_same_day(last_timestamp) and self.override_existing_today):
            timestamps[-1] = str(timestamps)
        else:
            timestamps.append(self.timestamp)
            if (len(timestamps) > self.NUMBER_DAYS_HISTORY):
                timstamps.pop(0)
        return timestamps

    def is_same_day(self, last_timestamp):
        if (last_timestamp == -1):
            return False
        current_date = datetime.fromtimestamp(self.timestamp).isocalendar()
        last_date = datetime.fromtimestamp(last_timestamp).isocalendar()
        return current_date == last_date

    def save_timestamps(self, timestamps):
        opened_file = open(self.file_name, 'w')
        for stamp in timestamps:
            opened_file.write("%s\n" % stamp)
        opened_file.close()
