from random import randint

def obfuscate(code):
    key = "@~pl-Steve28-lq~@"
    code = code.lower().replace("://", key).split("/")
    init, code = code[0].replace(key, "://"), code[1:]
    rescode = ""
    for block in code:
        rescode += "/"
        for i in list(block): 
            if i in ".": rescode += i
            else: rescode += chr((97+(ord(i)+1)%7) + 7*randint(0, 3))
    return init + rescode

def deobfuscate(code):
    key = "@~pl-Steve28-lq~@"
    code = code.lower().replace("://", key).split("/")
    init, code = code[0].replace(key, "://"), code[1:]
    rescode = ""
    for block in code:
        rescode += "/"
        for i in list(block):
            if i in ".": rescode += i
            else: rescode += chr(97+(ord(i)+1)%7)
    return init + rescode
