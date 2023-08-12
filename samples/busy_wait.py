"""
Loop which uses a custom `sleep` function.
"""

import time
from datetime import datetime, timedelta


def do_work():
    _ = 1 + 1


def sleep(seconds: float):
    end_time = datetime.now() + timedelta(seconds=seconds)

    while datetime.now() < end_time:
        pass


def problem():
    while True:
        do_work()
        sleep(0.001)


def solution():
    while True:
        do_work()
        time.sleep(0.001)
