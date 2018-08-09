class Proxy:
    def run(self):
        pass

# Our Proxy (IO) Monad implementation
class GetLine(Proxy):
    def run(self):
        return raw_input("")

class PutLine(Proxy):
    def __init__(self, line):
        self.line = line

    def run(self):
        print self.line

# Pure Proxy interface
def getLine():
    return GetLine()

def putLine(line):
    return PutLine(line)


def makeGreetingAndPutLine(name):
    return putLine("Hello, " + name)

getLineProxy = getLine()
name = getLineProxy.run()
putLineProxy = makeGreetingAndPutLine(name)
putLineProxy.run()
