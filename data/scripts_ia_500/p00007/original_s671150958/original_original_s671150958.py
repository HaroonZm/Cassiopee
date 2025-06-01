import math
f=100000
for i in range ( int ( input ( ) ) ):
    f=f*1.05
    f=int(math.ceil(f/1000)*1000)
    
print( f )