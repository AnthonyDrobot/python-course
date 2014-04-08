def find(a,b,c):
    if (a>b<c or a>c<b):
        return a
    elif (b>a<c or b>c<a):
        return b
    elif (c>b<c or c>a<b):
        return c

    assert find(1,3,5) == 3
    assert find(3,1,5) == 3
    assert find(2,6,4) == 3
    assert find(1,1,1) == 1
