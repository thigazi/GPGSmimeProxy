import logging
import Milter
from Milter.utils import parseaddr
from yaml import safe_load
from os.path import join
from pathlib import Path
from sys import argv
from email.message import Message
from re import search as re_search

logging.basicConfig(
    filename='/tmp/QFilterLog.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Mail Filter to handle encrypted Mails S/Mime and GPG


class QFilter(Milter.Base):
    def __init__(self):
        pfad = str(Path(__name__).resolve().parent)
        self.__from_domains = None
        self.id = Milter.uniqueID()

        self.__lg = logging.getLogger('qfilter_engine')


if __name__ == '__main__':
    pass
