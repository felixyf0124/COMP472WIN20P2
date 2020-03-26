class Writer:
    def __init__(self, content):
        self.content = content

    def outputWriter(self):
        filename = "output.txt"
        file = open(filename, "w+")
        file.write(self.content)
        file.close
