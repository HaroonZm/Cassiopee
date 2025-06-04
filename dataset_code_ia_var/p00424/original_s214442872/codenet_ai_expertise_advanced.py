from functools import partial
from operator import itemgetter

def convert(infile, outfile, n):
    dictionary = dict(map(str.split, (infile.readline() for _ in range(n))))
    m = int(infile.readline())
    get_value = partial(dictionary.get, default=None)
    input_words = (infile.readline().split()[0] for _ in range(m))
    outputs = (dictionary.get(word, word) for word in input_words)
    outfile.write(''.join(outputs) + '\n')

def run(infile, outfile):
    for n in map(int, iter(infile.readline, '0\n')):
        if n == 0:
            break
        convert(infile, outfile, n)

if __name__ == "__main__":
    import sys
    run(sys.stdin, sys.stdout)