def convert(infile, outfile, n):
    dictionary = {}
    for i in range(n):
        key, val = infile.readline().split()
        dictionary[key] = val
    m = int(infile.readline())
    for j in range(m):
        x = infile.readline().split()[0]
        outfile.write(dictionary.get(x, x))
    print >>outfile

def run(infile, outfile):
    while True:
        n = int(infile.readline())
        if n == 0:
            break
        convert(infile, outfile, n)

if __name__ == "__main__":
    import sys
    run(sys.stdin, sys.stdout)