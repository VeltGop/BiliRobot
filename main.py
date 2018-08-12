#!/usr/bin/python3
import signal
from util.log import Log
from service.msg import MsgService

log = Log('main')
msgService = MsgService()


def exitHandler(signum, frame):
    log.success('请等待 Service 退出...')
    msgService.stop()
    log.success('msgService已退出。')


if __name__ == '__main__':
    msgService.start()

    signal.signal(signal.SIGINT, exitHandler)
    signal.signal(signal.SIGTERM, exitHandler)
