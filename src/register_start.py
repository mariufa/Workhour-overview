from timestamp_handler import TimestampHandler
from time import time


if __name__ == '__main__':
    regsiter_start_file_name = "workhour_start.txt"
    now = time()
    handler = TimestampHandler(regsiter_start_file_name, now, False)
    handler.register_timestamp()
    
