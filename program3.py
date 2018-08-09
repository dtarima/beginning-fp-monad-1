class Proxy:
    def run(self):
        pass

class Bind(Proxy):
    def __init__(self, proxy, mapper):
        self.proxy = proxy
        self.mapper = mapper

    def run(self):
        return self.mapper(self.proxy.run()).run()

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
def bind(proxy, mapper):
    return Bind(proxy, mapper)

def getLine():
    return GetLine()

def putLine(line):
    return PutLine(line)

# Main program logic
def makeGreetingAndPutLine(name):
    return putLine("Hello, " + name)

print "START PURE PART"
program = bind(getLine(), makeGreetingAndPutLine)
print "START IMPURE PART"
program.run()
print "END"
