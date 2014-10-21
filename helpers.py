def read(filename):
    f = open(filename, "r")
    code = f.read()
    f.close()
    return code

def cleanup(code):
    return filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code)

def buildbracemap(code):
    temp_bracestack, bracemap = [], {}
    for position, command in enumerate(code):
        if command == "[":
            temp_bracestack.append(position)

        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap
