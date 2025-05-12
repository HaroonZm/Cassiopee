n, m = map( int, raw_input().strip().split() )
data = map( int, raw_input().strip().split() )

ans = 0

freq1 = [0] * ( max( data ) + 1 )
for x in data:
	freq1[ x ] += 1

freq2 = [0] * m
freq3 = [0] * m

for i in range( len( freq1 ) ):
	freq2[ i % m ] += freq1[i]
	freq3[ i % m ] += 2 * ( freq1[i] / 2 )

for i in range(m) :
	if ( i + i ) % m == 0:
		ans += freq2[i] / 2
	else:
		mx = 0
		val = min( freq2[i], freq2[m-i] )
		ans += val
		ans += min( freq3[i], freq2[i] - val ) / 2
		ans += min( freq3[m-i], freq2[m-i] - val ) / 2
		freq2[i] = freq2[ m-i ] = 0
		freq3[i] = freq3[ m-i ] = 0

print ans