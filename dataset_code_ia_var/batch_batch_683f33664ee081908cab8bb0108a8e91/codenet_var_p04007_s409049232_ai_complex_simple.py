from functools import reduce
from itertools import cycle, repeat, starmap, product
H,W=map(int,input().split())
Ass=[input()for _ in range(H)]
toggle=lambda n,p:[p[-1::-1]if i%2 else p for i,p in enumerate(repeat(['#']+['.']*(n-1),H))]
redss=list(map(lambda a: list(a[1]) if a[0]%2 else list(a[2]),enumerate(zip(['#']+['.']*(W-1) for _ in range(H)), (['#']*(W-1)+['.'] for _ in range(H)))))
bluess=list(map(lambda a: list(a[2]) if a[0]%2 else list(a[1]),enumerate(zip((['.']+['#']*(W-1) for _ in range(H)), (['.']*(W-1)+['#'] for _ in range(H))))))
update=lambda arr,val: [list(map(lambda z:val[i][j] if z=='#'else arr[i][j],v))for i,v in enumerate(arr)]
redss=update(redss,Ass)
bluess=update(bluess,Ass)
print('\n'.join(map(''.join,redss))+'\n\n'+'\n'.join(map(''.join,bluess)))