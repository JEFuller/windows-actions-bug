from multiprocessing import freeze_support
from sys import platform
from threading import Thread
from time import sleep
import click


class Runner(object):

    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            print("Running")
            sleep(1)

    def stop(self):
        if platform == "win32":
            from signal import CTRL_C_EVENT  # type: ignore
            from win32api import SetConsoleCtrlHandler  # type: ignore

            def ctrl_handler(_n: int):
                print("Caught Ctrl-C")
                return True

            SetConsoleCtrlHandler(ctrl_handler, True)

            kill(getpid(), CTRL_C_EVENT)  # type: ignore
        self.running = False


@click.command()
def hello():

    def _test():
        click.secho("Waiting", fg="blue")
        sleep(5)
        click.secho("Stopping", fg="blue")
        runner.stop()

    t = Thread(target=_test)
    t.start()

    click.secho("Starting runner", fg="blue")
    runner = Runner()
    runner.run()


if __name__ == '__main__':
    freeze_support()
    hello()
