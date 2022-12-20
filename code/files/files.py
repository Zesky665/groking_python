"""Use external files"""
def readfile(path):
    """Read first line from file"""
    f = open(path, 'r', encoding="utf-8")
    line = (f.readline()).strip()
    f.close()
    return line

def readline(path, line_num):
    """Read specific line from file"""
    f = open(path, 'r', encoding="utf-8")
    months = []
    for line in f:
        months.append(line.strip())
    f.close()
    return months[line_num]
