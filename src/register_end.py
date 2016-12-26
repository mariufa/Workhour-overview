from timestamp_handler import TimestampHandler
from time import time


if __name__ == '__main__':
    regsiter_end_file_name = "workhour_end.txt"
    now = time()
    handler = TimestampHandler(regsiter_end_file_name, now, True)
    handler.register_timestamp()
