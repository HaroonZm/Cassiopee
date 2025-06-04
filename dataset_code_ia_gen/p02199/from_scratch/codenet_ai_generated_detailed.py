# 入力を受け取る
A, B = map(int, input().split())
P, Q, R = map(int, input().split())

# 時間B分まではE869120君が学校に向かって歩き続ける
# E869120君の位置はB分後にP*Bメートル地点
# square1001君はA分後に追いかけ始めるため、その時のE869120君の位置はP*Aメートル

# B分以降、E869120君は忘れ物に気付き、分速Rで家に向かって戻る
# square1001君は分速Qで追いかけている

# 2人の位置関係を考える
# E869120君の位置 (t >= B):
#   S_e(t) = P*B - R*(t - B)
# square1001君の位置 (t >= A):
#   S_s(t) = Q*(t - A) + P*A = Q*(t - A) + P*A  （追いかけ始めた地点と時間を考慮）

# 2人が出会う時刻tを求める
# S_e(t) = S_s(t)
# P*B - R*(t - B) = Q*(t - A) + P*A

# この式をtについて解く
# P*B - R*t + R*B = Q*t - Q*A + P*A
# P*B + R*B - P*A + Q*A = Q*t + R*t
# (P*B + R*B) - (P*A - Q*A) = (Q + R)*t
# t = ((P*B + R*B) - (P*A - Q*A)) / (Q + R)

numerator = P*B + R*B - (P*A - Q*A)
denominator = Q + R
t = numerator / denominator

# 結果を出力（小数点以下十分な桁数で）
print(t)