from timestamp_handler import *
import time
from datetime import datetime

class WorkDay(object):

    def __init__(self, start_stamp, end_stamp):
        start = time.localtime(start_stamp)
        end = time.localtime(end_stamp)
        self.day = start.tm_mday
        self.month = start.tm_mon
        self.start_hour = start.tm_hour
        self.start_min = start.tm_min
        self.end_hour = end.tm_hour
        self.end_min = end.tm_min

    def __str__(self):
        return ("Workhours for: " +
                str(self.day) + "." + str(self.month) +
                " - " + self.int_to_string(self.start_hour) +
                ":" + self.int_to_string(self.start_min) +
                " --- " + self.int_to_string(self.end_hour) +
                ":" + self.int_to_string(self.end_min))

    def int_to_string(self, number):
        return (str(number) if number > 9 else "0" + str(number))

def load_work_days():
    work_days = []
    start_stamps = get_timestamps(REGISTER_START_FILE_NAME)
    end_stamps = get_timestamps(REGISTER_END_FILE_NAME)
    for start in start_stamps:
        for end in end_stamps:
            start = float(start)
            end = float(end)
            if is_same_day(start, end):
                work_days.append(WorkDay(start, end))
                break
    return work_days

def print_work_days(work_days):
    for day in work_days:
        print(day)

if __name__ == '__main__':
    work_days = load_work_days()
    print_work_days()
