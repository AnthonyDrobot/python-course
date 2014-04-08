import sys

result = 0
si = ''
fd = "1 2 3 3.45 abra_cadabra \n \n12"

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
        if line != "":
            yield line

def get_ints(gen):
    for line in gen:
        if line == int:
            yield line

def my_sum(gen):
    for line in gen:
        if line == int:
            yield result + line

def split_items(gen):
    for line in gen:
        if line == int:
            yield int(line)
        elif line == float:
            yield float(line)
        else:
            yield line

print list(iter_lines(fd))
print list(strip_spaces(iter_lines(fd)))
print list(drop_empty(fd))
print list(split_items(iter_lines(fd)))
print list(get_ints(fd))
print my_sum(fd)
print my_sum(get_ints(drop_empty(strip_spaces(iter_lines(fd)))))

# if __name__ == "__main__":
#     for line in iter_lines(open(sys.argv[0])):
#             print repr(line)