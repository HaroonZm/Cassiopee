import sys
#input = sys.stdin.readline

def io_generator():
	return input()
	
def ioByFile(fn='inputFile.txt'):
	with open(fn) as f:
		for line in f:
			yield line[:-1]

#+++++ +++++ +++++#
		
def main(a_io):
	c = a_io()
	tt='vowel'
	ff='consonant'
	boin=list('aiueo')
	ret=tt if c in boin else ff
	print(ret)
	
	
#+++++ +++++ +++++#

if __name__ == "__main__":
	io= lambda : io_generator()
	if sys.platform =='ios':
		testInput=ioByFile()
		io=lambda : next(testInput)
	main(io)