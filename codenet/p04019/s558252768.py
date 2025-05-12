def main23():
    strbuf = input("");
    flag = [];
    for i in range(4):
        flag.append(False);
    for i in range(len(strbuf)):
        if strbuf[i] == 'N':
            flag[0] = True;
        if strbuf[i] == 'W':
            flag[1] = True;
        if strbuf[i] == 'S':
            flag[2] = True;
        if strbuf[i] == 'E':
            flag[3] = True;
    if (flag[0] and not(flag[2])) or (flag[2] and not(flag[0])):
        print("No");
    elif (flag[1] and not(flag[3])) or (flag[3] and not(flag[1])):
        print("No");
    else:
        print("Yes");

if __name__ == '__main__':
    main23()