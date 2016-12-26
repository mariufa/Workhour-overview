from timestamp_handler import TimestampHandler
import time
from datetime import datetime

def get_timestamps(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def is_same_day(stamp_one, stamp_two):
    date_one = datetime.fromtimestamp(stamp_one).isocalendar()
    date_two = datetime.fromtimestamp(stamp_two).isocalendar()
    return date_one == date_two

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
