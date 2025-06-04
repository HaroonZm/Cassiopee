from sys import stdin
exec("x=1\nwhile x:\n S=0\n a=stdin.readline()\n if a.strip()=='0':break\n while a.strip():\n  try:S+=int(a[-2]);a=a[:-1]\n  except:a=a[:-1]\n print(S)")