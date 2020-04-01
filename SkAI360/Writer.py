class Writer:
    def __init__(self, filename):
        self.filename = filename

    def overwrite(self, content):
        file = open(self.filename, "w+", encoding="utf8")
        file.write(content)
        file.close

    def writeAtEOF(self, content):
        with open(self.filename, "a", encoding="utf8") as file:
            file.write(content)
            file.close


writer = Writer('output.txt')
writer.writeAtEOF('AAA')
