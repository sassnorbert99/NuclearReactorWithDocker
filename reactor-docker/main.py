import threading

from ReactorApp3 import Reactor
from controller.operator import Server


def main():
    reactor = Reactor()
    reactor_thread = threading.Thread(target=reactor.start_reactor)
    reactor_thread.start()
    server = Server(reactor)
    server.run_web_app()

if __name__ == '__main__':
    main()

#virtual env!!!
#package,
#https://tox.readthedocs.io/en/latest/

