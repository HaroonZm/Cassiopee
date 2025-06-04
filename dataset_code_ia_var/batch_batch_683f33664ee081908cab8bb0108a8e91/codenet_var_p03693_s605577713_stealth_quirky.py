_*Let colors:=input().split()
exec('r,g,b=[int(i)for i in colors];print("NO" if(10*g+b)%4 else"YES")')