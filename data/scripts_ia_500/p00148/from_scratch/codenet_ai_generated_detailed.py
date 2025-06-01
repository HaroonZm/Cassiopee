# クラス人数定数
NUM_STUDENTS = 39

def find_keeper(candies):
    """
    与えられたキャンディーの個数から、最後にキャンディーを取る生徒番号を求める関数。
    
    アプローチ：
    - 生徒は 3C01 ～ 3C39 の番号を持つ。
    - キャンディーは、生徒番号の順番に一人一つずつ取っていく。
    - キャンディー数が生徒数より多ければ、繰り返し順番に取ることになる。
    - 最後のキャンディーを取った生徒が「クラス旗」を保管する。
    - キャンディーの個数を 39 で割った余りから生徒番号を決定。
      余りが0の場合は39番目（3C39）となる。
    
    Parameters:
        candies (int): キャンディーの個数
    
    Returns:
        str: 最後にキャンディーを取る生徒の番号（例: "3C11"）
    """
    remainder = candies % NUM_STUDENTS
    # 余りが0なら生徒番号は39番
    student_number = remainder if remainder != 0 else NUM_STUDENTS
    
    # 生徒番号は1桁なら0パディングで2桁にする
    student_str = f"{student_number:02d}"
    return f"3C{student_str}"

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    candies = int(line)
    print(find_keeper(candies))