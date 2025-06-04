class State:
 def __init__(self, val):
  self.value = val

def process(inp, ctx):
 l = inp.split(',')
 if ctx['cur'] == l[0]:
  ctx['cur'] = l[1]
 elif ctx['cur'] == l[1]:
  ctx['cur'] = l[0]

current = State('A'); context = {'cur': current.value}
while 1:
 try:
  line = input()
  process(line, context)
  current.value = context['cur']
 except:
  break
print(getattr(current, 'value'))