h,w=map(int,input().split())
print(-(-h*w//2) if h*w>=h+w else 1)