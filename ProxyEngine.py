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
    filename='/tmp/PEngineLog.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Proxy for outgoing Mails


class PEngine(Milter.Base):
    def __init__(self):
        pfad = str(Path(__name__).resolve().parent)
        self.__keyFolder = join(pfad, 'keyFolder')
        self.id = Milter.uniqueID()

        self.__lg = logging.getLogger('proxy_engine')

    @Milter.noreply
    def envfrom(self, mailfrom, *str):
        pass

    def chgheader(self, field, idx, value):
        pass

    def replacebody(self, body):
        pass
