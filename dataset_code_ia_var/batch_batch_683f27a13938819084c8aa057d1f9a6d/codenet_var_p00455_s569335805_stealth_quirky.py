import datetime as DateTimeMod

def __run_the_clock__(timez):
    _t = [*map(int, timez.split())]
    _i, _o = _t[:3], _t[3:]
    times_as_words = ['hour', 'minute', 'second']
    t1 = DateTimeMod.datetime(*(2000,1,1,*_i))
    t2 = DateTimeMod.datetime(*(2000,1,1,*_o))
    diff = (t2 - t1).seconds
    result_tuple = (diff//3600, (diff//60)%60, diff%60)
    return ' '.join(str(result_tuple[times_as_words.index(tp)]) for tp in times_as_words)

if __name__ == '__main__':
    for _ in range(3):
        print(__run_the_clock__(input()))