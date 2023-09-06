from logging.config import dictConfig
import logging
from logging import getLogger

from log import LOGGING


def main():
    dictConfig(LOGGING)

    root_logger = getLogger()
    req_logger = getLogger('requests')

    req_logger.info('useful')


if __name__ == '__main__':
    main()
