lines=[]
while True:
    s=input()
    if s=="END_OF_TEXT":
        break
    lines.append(s)
cur_line=0
cur_pos=0
buffer=""
buffer_type="" # "str" or "lf"
def move_a():
    global cur_pos
    cur_pos=0
def move_e():
    global cur_pos
    cur_pos=len(lines[cur_line])
def move_p():
    global cur_line,cur_pos
    if cur_line>0:
        cur_line-=1
        cur_pos=0
    else:
        cur_pos=0
def move_n():
    global cur_line,cur_pos
    if cur_line+1<len(lines):
        cur_line+=1
        cur_pos=0
    else:
        cur_pos=0
def move_f():
    global cur_line,cur_pos
    if cur_pos<len(lines[cur_line]):
        cur_pos+=1
    else:
        if cur_line+1<len(lines):
            cur_line+=1
            cur_pos=0
def move_b():
    global cur_line,cur_pos
    if cur_pos>0:
        cur_pos-=1
    else:
        if cur_line>0:
            cur_line-=1
            cur_pos=len(lines[cur_line])
def cmd_d():
    global lines,cur_line,cur_pos
    if cur_pos<len(lines[cur_line]):
        lines[cur_line]=lines[cur_line][:cur_pos]+lines[cur_line][cur_pos+1:]
    else:
        if cur_line+1<len(lines):
            lines[cur_line]+=lines[cur_line+1]
            lines.pop(cur_line+1)
def cmd_k():
    global buffer,buffer_type,lines,cur_line,cur_pos
    if cur_pos<len(lines[cur_line]):
        buffer=lines[cur_line][cur_pos:]
        buffer_type="str"
        lines[cur_line]=lines[cur_line][:cur_pos]
        cur_pos=len(lines[cur_line])
    else:
        if cur_line+1<len(lines):
            buffer_type="lf"
            cmd_d()
def cmd_y():
    global buffer,buffer_type,lines,cur_line,cur_pos
    if buffer=="":
        return
    if buffer_type=="lf":
        l_before=lines[cur_line][:cur_pos]
        l_after=lines[cur_line][cur_pos:]
        lines[cur_line]=l_before
        lines.insert(cur_line+1,l_after)
        cur_line+=1
        cur_pos=0
    else:
        l=lines[cur_line]
        lines[cur_line]=l[:cur_pos]+buffer+l[cur_pos:]
        cur_pos+=len(buffer)
while True:
    c=input()
    if c=='-':
        break
    if c=='a':
        move_a()
    elif c=='e':
        move_e()
    elif c=='p':
        move_p()
    elif c=='n':
        move_n()
    elif c=='f':
        move_f()
    elif c=='b':
        move_b()
    elif c=='d':
        cmd_d()
    elif c=='k':
        cmd_k()
    elif c=='y':
        cmd_y()
for line in lines:
    print(line)