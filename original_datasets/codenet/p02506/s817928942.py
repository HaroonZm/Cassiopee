import sys

def solve():
    t =	raw_input()
    strr = ""
    total = 0
    while True:
	strr = raw_input()
	if strr	== "END_OF_TEXT":
            print total
            return
	single = strr.split()
#        print single                                                           
        for i in single:
	    if i.lower() == t:
		total += 1

if __name__ == "__main__":
    solve()