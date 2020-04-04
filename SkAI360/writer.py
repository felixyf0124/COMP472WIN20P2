import os


class Writer:
    def __init__(self, filename):
        self.filename = 'output/' + filename
        # if no dirctory then auto create
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    # overwrite content
    def overwrite(self, content):
        file = open(self.filename, "w+", encoding="utf8")
        file.write(content)
        file.close

    # write to the end of the file
    def writeAtEOF(self, content):
        with open(self.filename, "a", encoding="utf8") as file:
            file.write(content)
            file.close
