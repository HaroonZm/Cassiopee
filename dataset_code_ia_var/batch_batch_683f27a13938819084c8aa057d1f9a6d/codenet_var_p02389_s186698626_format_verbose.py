#!/usr/bin/env python

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_C

if __name__ == '__main__':

    rectangle_width, rectangle_height = map(int, raw_input().split())

    rectangle_area = rectangle_width * rectangle_height

    rectangle_perimeter = 2 * (rectangle_width + rectangle_height)

    print rectangle_area, rectangle_perimeter