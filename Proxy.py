import Milter
from Milter.utils import parseaddr
from yaml import safe_load
from os.path import join
from pathlib import Path
from sys import argv
from email.message import Message
from re import search as re_search


class Engine(Milter.Base):
    def __init__(self):
        pfad = str(Path(__name__).resolve().parent)
        self.__from_domains = None
        self.id = Milter.uniqueID()
        self.__id_from_to_domain = {}

        with open(join(pfad, 'settings.yml'), 'r') as cfgFile:
            cfg = safe_load(cfgFile)

        self.__from_domRegEx = '('
        self.__from_domains = cfg['from_domains']

        for i in range(len(cfg['from_domains'])):
            if i + 1 == len(cfg['from_domains']):
                self.__from_domRegEx += cfg['from_domains'][i].replace(
                    '.', '\\.') + ')'

            else:
                self.__from_domRegEx += cfg['from_domains'][i].replace(
                    '.', '\\.') + '|'

        print(self.__from_domRegEx)

    @Milter.noreply
    def envfrom(self, mailfrom, *str):
        self.__id_from_to_domain[self.id] = False
        # incoming mail, mail filter
        if re_search(self.__from_domRegEx, mailfrom) is None:
            self.__id_from_to_domain[self.id] = True

        return Milter.CONTINUE

    def chgheader(self, field, idx, value):
        if self.__id_from_to_domain[self.id]:
            pass

    def replacebody(self, body):
        if self.__id_from_to_domain[self.id]:
            pass
