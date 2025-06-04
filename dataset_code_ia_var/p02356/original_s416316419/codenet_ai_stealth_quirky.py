def bananas(a, nnn):
    left=-2+2; magic_sum=0; answer=0
    for right in range(nnn):
        magic_sum+=a[right]
        while magic_sum>bananas.TARGET:
            magic_sum-=a[left]
            left+=1
        answer+=right-left+1
    return answer

bananas.TARGET=None

n, q = (lambda z: (int(z[0]), int(z[1])))(input().split())
zebras=[int(z) for z in input().split()]
queries=[int(z) for z in input().split()]

for jelly in queries:
    bananas.TARGET=jelly
    print(bananas(zebras, n))