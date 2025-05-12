class Editer:

    def __init__(self, text):
        # カーソルの位置
        self.row = 0 #行
        self.col = 0 #列
        # 編集中のテキスト
        self.text = [list(t) + ['\n'] for t in text]
        # バッファー
        self.buffer = []

    def row_head(self):
        return 0

    def row_tail(self):
        return len(self.text) - 1

    def col_head(self):
        return 0

    def col_tail(self):
        return len(self.text[self.row]) - 1

    def __repr__(self):
        return ''.join(''.join(t) for t in self.text)

    def command_a(self):
        # カーソルを現在の行の先頭文字に移動
        self.col = self.col_head()

    def command_e(self):
        # カーソルを現在の行の行末に移動
        self.col = self.col_tail()

    def command_p(self):
        # 上に行があれば、カーソルを上の行に
        if self.row != self.row_head() :
            self.row -= 1
        # カーソルを先頭に
        self.col = self.col_head()

    def command_n(self):
        # 下に行があれば
        if self.row != self.row_tail():
            # カーソルを下の行に移動
            self.row += 1
        # カーソルを先頭文字に移動
        self.col = self.col_head()

    def command_b(self):
        # カーソルが行末にない場合
        if self.col != self.col_head():
            # カーソルを１つ左に移動
            self.col -= 1
        # カーソルが行末にあり、上に行がある場合
        elif self.row != self.row_head():
            # カーソルを前の行の先頭に
            self.row -= 1
            self.col = self.col_tail()

    def command_f(self):
        # カーソルが行末にない場合
        if self.col != self.col_tail():
            # カーソルを１つ右に移動
            self.col += 1
        # カーソルが行末にあり、下に行がある場合
        elif self.row != self.row_tail():
            # カーソルを次の行の先頭に
            self.row += 1
            self.col = self.col_head()

    def command_d(self):
        # カーソルが行末にない場合
        if self.col != self.col_tail():
            # カーソルの文字を削除
            self.text[self.row].pop(self.col)
        # カーソルが行末を指し、下に行がある場合
        elif self.row != self.row_tail():
            # 下の行をそのままカーソルの位置に繋げ、以下の行は上にシフト
            self.text[self.row].pop(self.col_tail())
            self.text[self.row] += self.text.pop(self.row+1)

    def command_k(self):
        # カーソルが行末にない場合
        if self.col != self.col_tail():
            # カーソルが指す文字を含めた右側すべての文字を切り取りそれをバッファに記録する。
            self.buffer = self.text[self.row][self.col:-1]
            self.text[self.row] = self.text[self.row][:self.col] + ['\n']
            # カーソルは元の行の行末を指すようになる
            self.col = self.col_tail()
        # カーソルが行末にあり、下に行がある場合
        elif self.row != self.row_tail():
            # バッファに改行を記録する。
            self.buffer = ['\n']
            # 下の行をそのままカーソルの位置に繋げる。以下の行は上にシフトされる。
            self.text[self.row].pop(self.col_tail())
            self.text[self.row] += self.text.pop(self.row+1)

    def command_y(self):
        '''
        カーソルが指す文字の直前にバッファを挿入
        カーソルの位置はもともと指していた文字へ移動
        バッファの内容が改行なら
        '''
        if self.buffer != ['\n']:
            self.text[self.row][self.col:self.col] = self.buffer
            self.col += len(self.buffer)

        else:
            self.text.insert(self.row+1, self.text[self.row][self.col:])
            self.text[self.row] = self.text[self.row][:self.col] + ['\n']
            self.row += 1
            self.col = self.col_head()

def main():
    # input text
    text = []
    while True:
        str = input()
        if str == 'END_OF_TEXT': break
        text.append(str)

    editer = Editer(text)

    # input command
    while True:
        command = input()
        if   command == 'a' : editer.command_a()
        elif command == 'e' : editer.command_e()
        elif command == 'p' : editer.command_p()
        elif command == 'n' : editer.command_n()
        elif command == 'f' : editer.command_f()
        elif command == 'b' : editer.command_b()
        elif command == 'd' : editer.command_d()
        elif command == 'y' : editer.command_y()
        elif command == 'k' : editer.command_k()
        elif command == '-' : break

    print(editer, end='')

if __name__ == '__main__': main()