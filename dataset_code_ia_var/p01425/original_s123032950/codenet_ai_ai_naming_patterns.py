import sys
_input_line = sys.stdin.readline

_GRAVITY = 9.8
_EPSILON = 1e-10

def _vertical_position(_initial_vy, _time):
    return _initial_vy * _time - _GRAVITY / 2 * _time * _time

def _positional_relation(_height, _low, _high):
    if _height < _low + _EPSILON:
        return -1
    if _height > _high - _EPSILON:
        return 1
    return 0

def _trajectory_possible(_target_x, _target_y):
    if _target_x == 0:
        return False
    _quadratic_a = _GRAVITY * _GRAVITY / 4
    _quadratic_b = _GRAVITY * _target_y - _VELOCITY * _VELOCITY
    _quadratic_c = _target_x * _target_x + _target_y * _target_y
    _discriminant = _quadratic_b * _quadratic_b - 4 * _quadratic_a * _quadratic_c
    if _discriminant < -_EPSILON:
        return False
    if -_EPSILON <= _discriminant < 0:
        _discriminant = 0
    for _directional in [-1, 1]:
        _root = (-_quadratic_b + _directional * _discriminant ** 0.5) / (2 * _quadratic_a)
        if _root <= 0:
            continue
        _time_travel = _root ** 0.5
        _vx = _target_x / _time_travel
        _vy = _target_y / _time_travel + _GRAVITY / 2 * _time_travel
        if _vertical_position(_vy, _TARGET_X / _vx) < _TARGET_Y - _EPSILON:
            continue
        _time_peak = _vy / _GRAVITY
        _x_peak = _vx * _time_peak
        _y_peak = _vertical_position(_vy, _time_peak)
        for _obst_left, _obst_bottom, _obst_right, _obst_top in _OBSTACLE_LIST:
            _left_status = _positional_relation(_vertical_position(_vy, _obst_left / _vx), _obst_bottom, _obst_top)
            _right_status = _positional_relation(_vertical_position(_vy, _obst_right / _vx), _obst_bottom, _obst_top)
            if _left_status * _right_status <= 0:
                break
            if _obst_left <= _x_peak <= _obst_right:
                _mid_status = _positional_relation(_y_peak, _obst_bottom, _obst_top)
                if _left_status * _mid_status <= 0:
                    break
        else:
            return True
    return False

_OBSTACLE_COUNT, _VELOCITY, _TARGET_X, _TARGET_Y = map(int, _input_line().split())
_OBSTACLE_LIST = []
for _ in range(_OBSTACLE_COUNT):
    _obst_left, _obst_bottom, _obst_right, _obst_top = map(int, _input_line().split())
    _obst_right = min(_obst_right, _TARGET_X)
    if _obst_left <= _TARGET_X:
        _OBSTACLE_LIST.append((_obst_left, _obst_bottom, _obst_right, _obst_top))

if _TARGET_X == 0:
    if _VELOCITY * _VELOCITY / (2 * _GRAVITY) < _TARGET_Y - _EPSILON:
        print('No')
        exit()
    for _obst_left, _obst_bottom, _obst_right, _obst_top in _OBSTACLE_LIST:
        if _obst_bottom < _TARGET_Y:
            print('No')
            exit()
    print('Yes')
    exit()

if _trajectory_possible(_TARGET_X, _TARGET_Y):
    print('Yes')
    exit()

for _obst_left, _obst_bottom, _obst_right, _obst_top in _OBSTACLE_LIST:
    if _trajectory_possible(_obst_left, _obst_top) or _trajectory_possible(_obst_right, _obst_top):
        print('Yes')
        exit()
print('No')