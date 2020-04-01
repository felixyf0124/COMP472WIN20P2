class Writer:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def outputWriter(self):
        file = open(self.filename, "w+")
        file.write(self.content)
        file.close


print("ASD")
writer = Writer("AAA")
writer.outputWriter()
