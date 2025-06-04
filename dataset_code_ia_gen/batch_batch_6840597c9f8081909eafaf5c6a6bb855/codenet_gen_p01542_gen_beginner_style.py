s=input()

candidates=[]
chars=['0','1','+','-','*','(',')']
for ch in s:
 if ch=='.':
  candidates.append(chars)
 else:
  candidates.append([ch])

from itertools import product

def is_digit(c):
 return c=='0' or c=='1'

def tokenize(expr):
 tokens=[]
 i=0
 while i<len(expr):
  c=expr[i]
  if c in '01+-*()':
   tokens.append(c)
   i+=1
  else:
   return None
 return tokens

def to_postfix(tokens):
 prec={'*':2,'+':1,'-':1}
 output=[]
 stack=[]
 for t in tokens:
  if t in '01':
   output.append(t)
  elif t in '+-*':
   while stack and stack[-1]!='(' and prec.get(stack[-1],0)>=prec[t]:
    output.append(stack.pop())
   stack.append(t)
  elif t=='(':
   stack.append(t)
  elif t==')':
   while stack and stack[-1]!='(':
    output.append(stack.pop())
   if not stack:
    return None
   stack.pop()
  else:
   return None
 while stack:
  if stack[-1] in '()':
   return None
  output.append(stack.pop())
 return output

def eval_postfix(postfix):
 stack=[]
 for t in postfix:
  if t in '01':
   stack.append(int(t))
  else:
   if len(stack)<2:
    return None
   b=stack.pop()
   a=stack.pop()
   if t=='+':
    v=a+b
   elif t=='-':
    v=a-b
   elif t=='*':
    v=a*b
   else:
    return None
   if v<0 or v>=210: # 210 = 2^10
    return None
   stack.append(v)
 if len(stack)!=1:
  return None
 return stack[0]

def valid_number(s):
 if len(s)==0:
  return False
 for ch in s:
  if ch not in '01':
   return False
 return True

def parse_expression(expr):
 # check parentheses balanced
 cnt=0
 for c in expr:
  if c=='(':
   cnt+=1
  elif c==')':
   cnt-=1
   if cnt<0:
    return False
 if cnt!=0:
  return False
 # tokenize and convert to postfix
 tokens=tokenize(expr)
 if tokens is None:
  return False
 postfix=to_postfix(tokens)
 if postfix is None:
  return False
 val=eval_postfix(postfix)
 if val is None:
  return False
 return val

maxv=-1
for p in product(*candidates):
 expr=''.join(p)
 val=parse_expression(expr)
 if val is not False and val>maxv:
  maxv=val

print(maxv) if maxv!=-1 else print(-1)