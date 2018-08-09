def getLine():
    return raw_input("")

def putLine(line):
    print line


def makeGreeting(name):
    return "Hello, " + name

name = getLine()
greeting = makeGreeting(name)
putLine(greeting)
