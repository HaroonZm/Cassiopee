if __name__ == '__main__':
    n = int(input())
    moji =[[],[' ','.',',','!','?'],['c','a','b'],['f','d','e'],['i','g','h'],['l','j','k'],['o','m','n'],['s','p','q','r'],['v','t','u'],['z','w','x','y']]
    for _ in range(n):
        line = list(input().strip().replace('0',' ').split())
        ans = []
        for i in line:
            m = int(i[0])
            ans.append(moji[m][len(i)%len(moji[m])])
        print(''.join(ans))