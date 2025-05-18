n = int( raw_input() )
if n <= 100:
    list = map( int, raw_input().split(' ') )
    print ' '.join( map( str, list[::-1]) )