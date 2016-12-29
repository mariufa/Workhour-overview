from timestamp_handler import TimestampHandler
from time import time


if __name__ == '__main__':
    now = time()
    handler = TimestampHandler(REGISTER_END_FILE_NAME, now, True)
    handler.register_timestamp()
