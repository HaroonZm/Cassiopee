char_list = [ chr(ord('a')+num) for num in range( 26 ) ]
N = int(input())

def Base_10_to_n(X, n):
    if X % n != 0 and (int(X//n)):
        return Base_10_to_n(int(X//n), n)+str(char_list[((X%n)-1)%n])
    elif X % n == 0 and (int(X//n)):
        if X//n == 1:
            return str(char_list[((X%n)-1)%n])
        else:
            return Base_10_to_n(int((X-1)//n), n)+str(char_list[((X%n)-1)%n])
    return str(char_list[((X%n)-1)%n])

print(Base_10_to_n(N,26))