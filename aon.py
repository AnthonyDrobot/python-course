def line(string=[]):
    i=0
    s=0
    result=''
    for element in string:
        for eel in string:
            if (element == eel):
                i+=1
            if (i>=2):
                result+=element
            if (element == '#'):
                s+=1
        i=0
    if (s>=2):
        result+=result[-1:]
    s=0
    return result

    assert line("") == ""
    assert line("1") == ""
    assert line("11") == "1"
    assert line("11111") == "1"
    assert line("11#") == "1"
    assert line("11##") == "11" 
    assert line("##") == "" 
    assert line("11122234###55") == "1225"
