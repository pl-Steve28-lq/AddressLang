from random import randint

def obfuscator(code):
	key = "@~pl-Steve28-lq~@"
	code = code.lower().replace("://", key).split("/")
	init, code = code[0].replace(key, "://"), code[1:]
	rescode = ""
	for block in code:
		rescode += "/"
		for i in list(block): rescode += chr((97+(ord(i)+1)%7) + 7*randint(0, 3))
	return init + rescode
