class CompileError(Exception): pass

class AddressLang:
    def __init__(self, size=256, error=100000):
        self.value = [0]*size
        self.pointer = 0
        self.error = error
        self.result = ""

    def gV(self):
        return self.value[self.pointer]

    def cV(self, val):
        self.value[self.pointer] += val

    def mP(self, val):
        self.pointer += val

    def compile(self, code, debug=False):
        key = "@~pl-Steve28-lq~@"
        code = code.replace("://", key).split("/")
        init, code = code[0], code[1:]
        strict = init.split(key)[0] == "https"
        point = 0
        error = 0
        length = len(code)
        while point < length:
            c = code[point]
            if debug: print(c)
            res = self.compileBlock(c, strict, debug)
            if res: point = res-1
            point += 1
            error += 1
            if error == self.error: raise CompileError("Calculation count exceeded.")
        print(self.result, end='\n' if self.result else '')
        self.result = ""
            

    def compileBlock(self, code, strict, debug):
        if "." in code:
            codes = code.split(".")
            go, ifs = codes[:2]
            gores = self.compileBlock(go, strict, debug)
            if gores: return gores
            if self.value[self.pointer] != 0:
                ifres = self.compileBlock(ifs, strict, debug)
                if ifres: return ifres
        else:
            codelist = list(code)
            res = None
            for i in codelist:
                self.pointer %= len(self.value)
                asc = ord(i)
                if 97 <= asc <=122:
                    key = asc%7
                    if key == 6: self.cV(1)
                    if key == 0: self.cV(-1)
                    if key == 1: self.mP(1)
                    if key == 2: self.mP(-1)
                    if key == 3: self.result += chr(self.gV())
                    if key == 4: self.value[self.pointer] = ord(input()[0])
                    if key == 5: res =  self.value[self.pointer]
                else:
                    if strict: raise CompileError(f"Incorrect keyword {i} detected.")
            if res: return res

    def compilePath(self, path):
        with open(path) as f:
            self.compile(''.join(f.readlines()))
