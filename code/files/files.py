"""Use external files"""
def readfile(path):
    """Read first line from file"""
    f = open(path, 'r', encoding="utf-8")
    line = f.readline()
    f.close()
    return line
