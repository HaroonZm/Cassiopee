def shuffle(word, length):
	li = list(word)
	ad = li[0:length]
	li += ad
	del li[0:length]
	return ''.join(li)

while True:
	str = input()
	if str == '-':
		break
	num = int(input())
	
	for i in range(num):
		rn = int(input())
		str = shuffle(str, rn)
		
	print(str)