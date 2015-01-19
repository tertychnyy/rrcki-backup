import logging
import os

from BKPConfig import BKPConfig


class BKPLogger:
    def __init__(self):
        self.logdir = BKPConfig().getLogDir()

    def getLogger(self, name):
        _logger = logging.getLogger(name)
        hdlr = logging.FileHandler(os.path.join(self.logdir, 'backup.log'))
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        _logger.addHandler(hdlr)
        _logger.setLevel(logging.DEBUG)
        return _logger