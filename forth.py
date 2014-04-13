stack =()

def eval_forth(file):
    ch = file.read(1)
    res = ""
    while ch != '':
        if ch == '/n':
            yield res
            res = ""
        elif ch == '#':
            yield res
            res = ""
        else:
            res += ch
            ch = fd.read(1)
    yield res



eval_forth('forth.py')