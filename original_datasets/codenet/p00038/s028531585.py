import sys

def heaven():
    result_dic = {}
    check_num_lis = []
    for i in range(5):
        check_num = card_lis[0]
        if not check_num in check_num_lis:
            for card in card_lis[1:]:
                if card == check_num:
                    if not card in result_dic:
                        result_dic[card] = 2
                    else:
                        result_dic[card] = result_dic[card] + 1
            check_num_lis.append(check_num)
        card_lis.append(check_num)
        del card_lis[0]
    
    suicide(result_dic)
    
def suicide(result_dic):
    result = result_dic.values()
    result.sort()
    if result == [2]:
        print 'one pair'
    elif result == [2,2]:
        print 'two pair'
    elif result == [3]:
        print 'three card'
    elif result == [4]:
        print 'four card'
    elif result == [2,3]:
        print 'full house'
    elif not result:
        card_lis.sort()
        if card_lis == [1,10,11,12,13]:
            print 'straight'
        else:
            check_num = card_lis[0]
            for card in card_lis:
                if card == check_num:
                    check_num = card + 1
                else:
                    print 'null'
                    break
            else:
                print 'straight'

for input_line in sys.stdin:
    card_lis = [int(char) for char in input_line.split(',')]
    heaven()