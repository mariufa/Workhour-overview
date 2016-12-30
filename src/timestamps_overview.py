from timestamp_handler import *
import time
from datetime import datetime

class WorkDay(object):

    def __init__(self, start_stamp, end_stamp):
        start = time.localtime(start_stamp)
        end = time.localtime(start_stamp)
        self.day = start.tm_mday
        self.month = start.tm_mon
        self.start_hour = start.tm_hour
        self.start_min = start.tm_min
        self.end_hour = end.tm_hour
        self.end_min = end.tm_min

    def __str__(self):
        return ("Workhours for: " +
                str(self.day) + "." + str(self.month) +
                " - " + str(self.start_hour) +
                ":" + str(self.start_min) +
                " --- " + str(self.end_hour) +
                ":" + str(self.end_min))

work_days = []

if __name__ == '__main__':
    start_stamps = get_timestamps(REGISTER_START_FILE_NAME)
    end_stamps = get_timestamps(REGISTER_END_FILE_NAME)
    for start in start_stamps:
        for end in end_stamps:
            start = float(start)
            end = float(end)
            if is_same_day(start, end):
                work_days.append(WorkDay(start, end))
                break

    for day in work_days:
        print(day)
