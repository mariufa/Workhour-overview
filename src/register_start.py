from datetime import datetime
from time import tim


file_name = "work_start.txt";

def set_file_name(name):
    file_name = name

def register_start():
    timestamp = time()
    file_work_start = open(file_name)
    last_timestamp = get_last_time_stamp()
    if not is_same_day(timestamp, last_timestamp):
        save_timestamp(timestamp)

def get_last_time_stamp():
    file_work_start = open(file_name)
    last_line = get_last_line()
    if (last_line):
        return float(last_line)
    else:
        return -1;

def get_last_line():
    last_line = None
    with open(file_name) file_work_start:
        for line in (line for line in file_work_start if line.rstrip('\n')):
            last_line = line
    return last_line


def is_same_day(timestamp, last_timestamp):
    current_date = datetime.fromtimestamp(timestamp).isocalendar()
    last_date = datetime.fromtimestamp(last_timestamp).isocalendar()
    return current_date == last_date

def save_timestamp(timestamp):
    with open(file_name) as file_work_start:
        file_work_start.write(timestamp)

if __name__ == "__main__":
    register_start()
