from multiprocessing import freeze_support
from os import getpid, kill
from signal import CTRL_C_EVENT
from threading import Thread
from time import sleep

from win32api import SetConsoleCtrlHandler


class Runner(object):

    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            print("Running")
            sleep(1)

    def stop(self):

        def ctrl_handler(_n: int):
            print("Caught Ctrl-C")
            return True

        SetConsoleCtrlHandler(ctrl_handler, True)

        kill(getpid(), CTRL_C_EVENT)
        self.running = False


def hello():

    def _test():
        print('Starting test')
        sleep(5)
        print('Stopping runner')
        runner.stop()

    t = Thread(target=_test)
    t.start()

    print('Starting runner')
    runner = Runner()
    runner.run()


if __name__ == '__main__':
    freeze_support()
    hello()
