"""
Simplest tight loop which does absolutely nothing.
"""


def do_work():
    _ = 1 + 1


def problem():
    while True:
        do_work()


def solution():
    import time
    while True:
        do_work()
        time.sleep(0.001)


def do_disk_io_work():
    result = 1 + 1
    with open("temp.txt", "w") as _file:
        _file.write(str(result))


def disk_io():
    while True:
        do_disk_io_work()


def do_network_io_work():
    import http.client
    client = http.client.HTTPSConnection("google.com")
    client.request("GET", "/")
    client.getresponse()


def network_io():
    while True:
        do_network_io_work()
