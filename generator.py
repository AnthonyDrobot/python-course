import sys

si = ''
fl = open('gen.txt')
#fd = open(sys.argv[0])
#fd = input("1 2 3 3.45 abra_cadabra   \n\n12 ")
print fl

def iter_lines(fd):
    ch = fd.read(1)
    res = ""
    while ch != '':
        if ch == '/n':
            yield res
            res = ""
        else:
            res += ch
        ch = fd.read(1)
    yield res

def strip_spaces(gen):
    for line in gen:
        yield line.strip()

def drop_empty(gen):
    for line in gen:
        if line != '' and line != '\n':
            yield line

def get_ints(gen):
    for line in gen:
        words = str.split(line)
        for word in words:
            try:
                if isinstance(int(line), int):
                    yield int(line)
            except:
                pass

def my_sum(gen):
    for val in gen:
        result = 0
        result = result + int(val)
        yield result

def split_items(gen):
    for line in gen:
        words = str.split(line)
        for word in words:
            try:
                if isinstance(int(word), int):
                    #if line == int:
                    yield int(word)
                else:
                    yield word
            except:
                pass
            try:
                if isinstance(float(word), float):
                    #elif line == float:
                    yield float(word)
                else:
                    yield word
            except:
                pass
    yield line

print list(iter_lines(fl))
print '\n'
print list(strip_spaces(iter_lines(fl)))
print '\n'
print list(drop_empty(fl))
print '\n'
print list(split_items(iter_lines(fl)))
print '\n'
print list(get_ints(fl))
print '\n'
print list(my_sum([1, 2, 3, 12]))
print '\n'
print my_sum(get_ints(drop_empty(strip_spaces(iter_lines(fl)))))

# if __name__ == "__main__":
#     for line in iter_lines(open(sys.argv[0])):
#             print repr(line)