class Loader:
    def __init__(self, path):
        file = open(path, "r")
        lineNum = 0
        for line in file:
            lineNum += 1
        file.close()
        print(lineNum)
