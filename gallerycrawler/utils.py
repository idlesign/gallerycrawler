import logging


def setup_logging(level=logging.INFO):

    for item in ('urllib3', 'requests'):
        logging.getLogger(item).setLevel(logging.ERROR)

    logging.basicConfig(format='%(levelname)s: %(message)s', level=level)
