# coding:utf-8
import logging
import time
import os

cur_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')

if not os.path.exists(log_path):
        os.mkdir(log_path)


def __console(level, message):
        logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] - %(pathname)s] - %(levelname)s: %(message)s')
        fh = logging.FileHandler(logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()


def debug(message):
        __console('debug', message)


def info(message):
        __console('info', message)


def warning(message):
        __console('warning', message)


def error(message):
        __console('error', message)




