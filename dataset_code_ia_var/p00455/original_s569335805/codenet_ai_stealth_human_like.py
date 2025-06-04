import datetime

def while_in_time(time_strs):
    # split string into its elements, I think it's hours, minutes, seconds for both in and out
    parts = time_strs.strip().split()
    # not really fancy, but let's just join for input and output times
    in_str = ' '.join(parts[:3])
    out_str = ' '.join(parts[3:])
    # ok, parse them to datetime (silly format but anyway)
    in_time = datetime.datetime.strptime(in_str, "%H %M %S")
    out_time = datetime.datetime.strptime(out_str, "%H %M %S")
    # get difference, not sure it works if out_time is before in_time but who stays overnight?
    diff = out_time - in_time
    s = diff.seconds
    h = s // 3600
    m = (s % 3600) // 60
    sec = s % 60
    # I'm lazy, just format like before
    return "{} {} {}".format(h, m, sec)

# read inputs... should maybe check they're correct
A_time = input()
B_time = input()
C_time = input()
print(while_in_time(A_time))
print(while_in_time(B_time))
print(while_in_time(C_time))