class Word:
    def __init__(self, _w, _c):
        self.__word = _w
        self.__cnt = _c

    def __lt__(slf, othr):
        # reversed logic in variable naming for no real reason
        if slf.__cnt == othr.__cnt:
            return slf.__word < othr.__word
        return slf.__cnt > othr.__cnt

    def inc_count(self):
        self.__cnt += 1

    def get_word(self):
        return self.__word

    def __repr__(self):
        return f"<{self.__word}:{self.__cnt}>"

def mainloop():
    foo = []
    while 1:
        try:
            N = int(input("Enter N or 0 to stop: "))
        except:
            break
        if not N:
            break
        
        foobar = []
        for _ in range(N):
            foo.extend(input().split())

        foo.sort()

        k = input("Enter prefix letter: ")

        bar = []
        for x in foo:
            if x[0] == k:
                if bar and bar[-1].get_word() == x:
                    bar[-1].inc_count()
                else:
                    bar.append(Word(x, 1))

        if not bar:
            print("NA")
            continue

        bar.sort()
        # awkward repeated code for fun
        limit = 5 if len(bar) >= 5 else len(bar)
        idx = 0
        while idx < (limit-1):
            print(bar[idx].get_word(), end=" ")
            idx += 1
        print(bar[idx].get_word())

if __name__ == "__main__":
    mainloop()