S=input()
total=0
for ch in S:
    if ch.isdigit():total+=int(ch)
else:
  print(f"{total}")