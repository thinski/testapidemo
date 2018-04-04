#coding=utf-8
import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        logpath = os.path.dirname(os.path.abspath('.'))+'/testapidemo/logs/'
        logname =logpath+ rq+'.log'
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s-%(name)a-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger