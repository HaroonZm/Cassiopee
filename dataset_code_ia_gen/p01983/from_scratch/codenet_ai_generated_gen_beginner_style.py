def parse_hash(s):
    # 再帰的にハッシュ式をパースして木構造を返す
    # ノードは dict で { "type": "letter" or "op", "value": letter or op, "left": _, "right": _ }
    s = s.strip()
    if len(s) == 1 and s in "abcd":
        return {"type": "letter", "value": s}
    # 形式: [<op><hash><hash>]
    # 例: [+c[+a[^bd]]]
    if s[0] == "[" and s[-1] == "]":
        op = s[1]
        rest = s[2:-1]
        # restを2つのハッシュに分割する
        # 文字数だけでは割れないので括弧の深さで判断
        pos = 0
        depth = 0
        for i, ch in enumerate(rest):
            if ch == "[": depth += 1
            elif ch == "]": depth -= 1
            # depthが0になってから1文字目を2つに分ける
            if depth == 0:
                pos = i + 1
                break
        left_s = rest[:pos]
        right_s = rest[pos:]
        return {"type": "op", "value": op, "left": parse_hash(left_s), "right": parse_hash(right_s)}
    return None  # 不正な入力時用（使わない）

def eval_hash(node, pwd):
    # node構造体をパスワードpwd(文字列4桁)を用いて評価し，intを返す
    if node["type"] == "letter":
        # a,b,c,dはpwdの各桁を表す
        idx = ord(node["value"]) - ord("a")
        return int(pwd[idx])
    else:
        left_val = eval_hash(node["left"], pwd)
        right_val = eval_hash(node["right"], pwd)
        if node["value"] == "+":
            return left_val | right_val
        elif node["value"] == "*":
            return left_val & right_val
        elif node["value"] == "^":
            return left_val ^ right_val

def main():
    while True:
        S = input()
        if S == ".":
            break
        P = input()
        root = parse_hash(S)
        # 入力パスワードのハッシュ値を求める
        hval = eval_hash(root, P)
        # 同じハッシュ値になるパスワードの数を数える（0000から9999まで全探索）
        count = 0
        for i in range(10000):
            pwd = str(i).zfill(4)
            if eval_hash(root, pwd) == hval:
                count += 1
        print(hval, count)

main()