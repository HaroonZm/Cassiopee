N,W,D = map(int,input().split())

while W:
  cp = [[0,0,0,0] for _ in range(2*N+1)]	#始点x,始点y,長さx,長さy
  cp[0] = [0,0,W,D]
  
  for time in range(N):
    P,S = map(int,input().split())
    P -= 1
    ta = cp[P]
    S %= (ta[2]+ta[3])*2
    
    #カット処理
    #面積が小さいほうが番号が小さい
    
    #上辺
    if 0 <= S < ta[2]:
      if S < ta[2]/2:
        cp[time+1] = [ta[0],ta[1],S,ta[3]]
        cp[time+2] = [ta[0]+S,ta[1],ta[2]-S,ta[3]]
      else:
        cp[time+1] = [ta[0]+S,ta[1],ta[2]-S,ta[3]]
        cp[time+2] = [ta[0],ta[1],S,ta[3]]
        
    #右辺
    elif S < ta[2]+ta[3]:
      S -= ta[2]
      if S < ta[3]/2:
        cp[time+1] = [ta[0],ta[1],ta[2],S]
        cp[time+2] = [ta[0],ta[1]+S,ta[2],ta[3]-S]
      else:
        cp[time+1] = [ta[0],ta[1]+S,ta[2],ta[3]-S]
        cp[time+2] = [ta[0],ta[1],ta[2],S]
        
    #下辺
    elif S < ta[2]*2+ta[3]:
      S = ta[2]-(S-ta[2]-ta[3])
      if S < ta[2]/2:
        cp[time+1] = [ta[0],ta[1],S,ta[3]]
        cp[time+2] = [ta[0]+S,ta[1],ta[2]-S,ta[3]]
      else:
        cp[time+1] = [ta[0]+S,ta[1],ta[2]-S,ta[3]]
        cp[time+2] = [ta[0],ta[1],S,ta[3]]
        
    #左辺
    else:
      S = ta[3]-(S-ta[2]*2-ta[3])
      if S < ta[3]/2:
        cp[time+1] = [ta[0],ta[1],ta[2],S]
        cp[time+2] = [ta[0],ta[1]+S,ta[2],ta[3]-S]
      else:
        cp[time+1] = [ta[0],ta[1]+S,ta[2],ta[3]-S]
        cp[time+2] = [ta[0],ta[1],ta[2],S]
        
    #カットされたやつのデータを消す
    del cp[P]
    
    
  #データ出力
  ansli = []
  for el in cp:
    ansli.append(el[2]*el[3])
  ansli.sort()
  print(*ansli)
  
  N,W,D = map(int,input().split())