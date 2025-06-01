def convert(infile, outfile, n):
    dictionary = dict(next(infile).split() for _ in range(n))
    m = int(next(infile))
    words = (next(infile).split()[0] for _ in range(m))
    outfile.writelines(dictionary.get(word, word) + '\n' for word in words)

def run(infile, outfile):
    for line in infile:
        n = int(line)
        if n == 0:
            break
        convert(infile, outfile, n)

if __name__ == "__main__":
    import sys
    run(sys.stdin, sys.stdout)