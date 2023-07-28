from multiprocessing import freeze_support
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
