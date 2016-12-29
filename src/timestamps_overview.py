from timestamp_handler import *
import time
from datetime import datetime

class WorkDay(object):

    def __init__(self, start_stamp, end_stamp):
        start = time.localtime(float(start_stamp))
        end = time.localtime(float(start_stamp))
        self.day = start.tm_mday
        self.month = start.tm_mon
        self.start_hour = start.tm_hour
        self.start_min = start.tm_min
        self.end_hour = end.tm_hour
        self.end_min = end.tm_min

    def __str__(self):
        return ("Workhours for: " +
                self.day + "." + self.month +
                " - " + self.start_hour +
                ":" + self.start_min +
                " --- " + self.end_hour +
                ":" + self.end_min)

if __name__ == '__main__':
    regsiter_start_file_name = "workhour_start.txt"
    regsiter_end_file_name = "workhour_end.txt"
    start_stamps = get_timestamps(regsiter_start_file_name)
    end_stamps = get_timestamps(regsiter_end_file_name)
    for start in start_stamps:
        for end in end_stamps:
            start = float(start)
            end = float(end)
            if is_same_day(start, end):
                start_time = time.localtime(start)
                end_time = time.localtime(end)
                print("Workhours for ", start_time.tm_mday,
                        ".", start_time.tm_mon,
                        " - ", start_time.tm_hour,
                        ":", start_time.tm_min,
                        " --- ", end_time.tm_hour,
                        ":", end_time.tm_min, sep='')
                break
