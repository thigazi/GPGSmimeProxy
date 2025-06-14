from twisted.internet.interfaces import IAddress
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Echo(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write("Welcome there are currently %d open connections.\n" % (self.factory.numProtocols,))

    def connection(self,reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self,data):
        self.transport.write(data)


class QOTD(Protocol):

    def connectionMade(self):
        # self.factory was set by the factory's default buildProtocol:
        self.transport.write(self.factory.quote + '\r\n')
        self.transport.loseConnection()


class QOTDFactory(Factory):

    # This will be used by the default buildProtocol to create new protocols:
    protocol = QOTD

    def buildProtocol(self, addr):
        return QOTD()

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'


if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(QOTDFactory("configurable quote"))
    reactor.run()