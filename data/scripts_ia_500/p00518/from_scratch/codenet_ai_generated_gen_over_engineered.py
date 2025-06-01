class Member:
    J = 0b001
    O = 0b010
    I = 0b100

    @classmethod
    def all_members(cls):
        return [cls.J, cls.O, cls.I]

class ScheduleDay:
    def __init__(self, responsible_member_char: str):
        self.responsible = self.char_to_member(responsible_member_char)

    @staticmethod
    def char_to_member(c: str) -> int:
        if c == 'J': return Member.J
        elif c == 'O': return Member.O
        elif c == 'I': return Member.I
        else: raise ValueError(f"Invalid member char: {c}")

class ScheduleState:
    def __init__(self, key_holder_mask: int, day: int):
        self.key_holder_mask = key_holder_mask  # bitmask of who holds the key
        self.day = day

    def __hash__(self):
        return hash((self.key_holder_mask, self.day))

    def __eq__(self, other):
        return (self.key_holder_mask == other.key_holder_mask) and (self.day == other.day)

class SchedulePlanner:
    MOD = 10007
    ALL_MASK = 0b111  # All three members present bitmask

    def __init__(self, days: int, responsible: str):
        self.days = days
        self.schedule_days = [ScheduleDay(c) for c in responsible]
        self.dp = [{} for _ in range(days)]
        # dp[i][key_holder_mask] = number of ways
    
    def mask_includes(self, mask: int, member: int) -> bool:
        return (mask & member) != 0

    def valid_subsets(self, must_member: int):
        # generate all subsets of {J,O,I} which include the must_member
        subsets = []
        for s in range(1, 8):
            if (s & must_member) == 0:
                continue
            subsets.append(s)
        return subsets

    def has_common_member(self, mask1: int, mask2: int) -> bool:
        return (mask1 & mask2) != 0

    def plan(self) -> int:
        # 初期状態: day0 は鍵持ちは J 君(0b001)
        # 1日目の活動は必ず責任者が参加しなければならない
        first_responsible = self.schedule_days[0].responsible
        first_day_subsets = self.valid_subsets(first_responsible)

        for subset in first_day_subsets:
            if (subset & Member.J) == 0:
                # 鍵は最初 J 君が持っているので、参加者にJがいなければ鍵が渡せない
                continue
            # 鍵を誰が持ち帰っても良いが、次の日のDP用に鍵持ちは参加者の誰か (これをあとで設定します)
            # 初日は鍵持ちは誰でもよいので、鍵持ちは subset の中の誰か → キーは subset のビットマスクの説明になっている
            # しかし鍵は一人にしか渡せないので状態は鍵保持者1人のビット
            # なので dp[0][key_holder_mask] += 1 for those key_holder_mask in subset
            # しかし初期鍵持ちは J 君だが、活動後鍵は参加者の誰かに渡るので 
            # 活動中はJを持ってるが終了後は参加者の1人が持ってる
            # 初期鍵持ちは固定なので初回だけ特別に扱う

            # dp state は鍵持ち一人なので、 subset 内の1人ずつに鍵渡す遷移を考えるのが本質
            # なのでここでは subset は参加者全体
            for key_holder in [Member.J, Member.O, Member.I]:
                if (subset & key_holder) != 0:
                    # 1日目の鍵持ちは key_holder で、参加者 subset
                    # 鍵初期保持者は J だが、初日の活動参加にJがいないといけない（鍵はJが持ってるため）
                    # そうであるため subset must include J already 
                    self.dp[0][key_holder] = (self.dp[0].get(key_holder,0) + 1) % self.MOD

        # 2日目以降
        for day in range(1, self.days):
            responsible = self.schedule_days[day].responsible
            current_subsets = self.valid_subsets(responsible)
            prev_states = self.dp[day-1]
            current_dp = self.dp[day]
            for prev_key_holder, ways in prev_states.items():
                # prev_key_holder は前日の鍵持ち(1bit)
                for subset in current_subsets:
                    # 参加者 subset は責任者を含む
                    # 前日の鍵持ちは subset に含まれていなければ鍵の受け渡し不可
                    if (subset & prev_key_holder) == 0:
                        continue
                    # 鍵は subset 内の誰かに渡さなければならないから鍵の持ち帰りは subsetのメンバーから
                    for next_key_holder in [Member.J, Member.O, Member.I]:
                        if (subset & next_key_holder) != 0:
                            # 鍵持ちは必ず1人
                            current_dp[next_key_holder] = (current_dp.get(next_key_holder,0)+ ways) % self.MOD

        # 最終日は鍵持ち誰でも良いので全て合計
        result = 0
        final_dp = self.dp[self.days-1]
        for ways in final_dp.values():
            result = (result + ways) % self.MOD
        return result


def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())
    responsible = sys.stdin.readline().strip()

    planner = SchedulePlanner(N, responsible)
    print(planner.plan())

if __name__ == "__main__":
    main()