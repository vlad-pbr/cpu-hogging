"""
Waiting for results from a queue.
"""

from time import sleep
from threading import Thread
from queue import Queue
from random import choice

queue = Queue(maxsize=1)


def producer_thread():
    while True:
        queue.put(choice(["apple", "banana", "cherry"]))
        sleep(1)


def problem():
    Thread(target=producer_thread).start()
    while True:
        if not queue.empty():
            print(queue.get())


def solution():
    Thread(target=producer_thread).start()
    while True:
        print(queue.get())
