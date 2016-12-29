from timestamp_handler import *
from time import time


if __name__ == '__main__':
    now = time()
    handler = TimestampHandler(REGISTER_START_FILE_NAME, now, False)
    handler.register_timestamp()
