# 入力された英語の文章から指定された区切り文字で単語を切り出し、
# 3文字から6文字の単語を抽出して半角スペースで連結して出力するプログラム

def extract_words(sentence):
    # まず、区切り文字（空白、ピリオド、カンマ）を全て空白に置換する
    # これにより単語間が空白区切りのみに統一される
    for sep in ['.', ',', ' ']:
        sentence = sentence.replace(sep, ' ')
    
    # 空白で分割すると空文字も含まれる場合があるため
    # filterを使って空文字を除去し、リストで取得する
    words = list(filter(lambda w: w != '', sentence.split(' ')))
    
    # 単語の長さが3～6文字のものだけを抽出する
    filtered_words = [w for w in words if 3 <= len(w) <= 6]
    
    # 指定された条件に合う単語を半角スペースで連結して文字列で返す
    return ' '.join(filtered_words)

# メイン処理
if __name__ == '__main__':
    # 入力は1行の英語の文章（1024文字以下）
    line = input()
    result = extract_words(line)
    print(result)