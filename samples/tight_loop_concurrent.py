"""
Tight loop in two separate threads/processes.
"""

from multiprocessing import Process
from threading import Thread


def do_work():
    _ = 1 + 1


def problem():
    while True:
        do_work()


def spawn(items):
    for item in items:
        item.start()

    for item in items:
        item.join()


def spawn_threads():
    spawn([Thread(target=problem) for _ in range(2)])


def spawn_processes():
    spawn([Process(target=problem) for _ in range(2)])
