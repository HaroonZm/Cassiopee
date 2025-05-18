#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	R1, R2 = getlist()
	ans = R1 * R2 / (R1 + R2)
	print(ans)

if __name__ == '__main__':
	main()