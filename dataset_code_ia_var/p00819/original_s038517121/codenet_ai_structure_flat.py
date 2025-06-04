ans = []
for _ in range(int(input())):
    to_do = input()
    message = input().strip()
    for op in to_do[::-1]:
        if op == 'C':
            if len(message) >= 2:
                message = message[1:] + message[0]
            else:
                message = message
        if op == 'J':
            if len(message) >= 2:
                message = message[-1] + message[:-1]
            else:
                message = message
        if op == 'E':
            if len(message) == 1:
                message = message
            elif len(message) % 2:
                mid = len(message) // 2
                message = message[mid+1:] + message[mid] + message[:mid]
            else:
                mid = len(message) // 2
                message = message[mid:] + message[:mid]
        if op == 'A':
            message = message[::-1]
        if op == 'M':
            new = ''
            for ch in message:
                o = ord(ch)
                if o < 57 and o >= 48:
                    new += chr(o + 1)
                elif o == 57:
                    new += '0'
                else:
                    new += ch
            message = new
        if op == 'P':
            new = ''
            for ch in message:
                o = ord(ch)
                if o <= 57 and o > 48:
                    new += chr(o - 1)
                elif o == 48:
                    new += '9'
                else:
                    new += ch
            message = new
    ans.append(message)
for i in ans:
    print(i)