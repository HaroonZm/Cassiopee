#!/usr/bin/python

import re

def main():
    n = int(raw_input())
    s = raw_input()

    print n-min(map(lambda x: x.end()-x.start(), [re.search(r'^<*', s), re.search(r'>*$', s)]))

if __name__ == '__main__':
    main()