import sys

def count_patterns(line):
    joi=0
    ioi=0
    i=0
    while i<len(line)-3:
        chunk = line[i:i+3]
        if chunk=="JOI":
            joi+=1
        if chunk=="IOI":
            ioi=ioi+1
        i+=1
    return joi,ioi

def main():
    inp=sys.stdin
    for l in inp:
        a,b=count_patterns(l)
        print(a)
        print(b)

[main() for _ in [0]]