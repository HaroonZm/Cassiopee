import sys
_input_readline = sys.stdin.readline
_output_write = sys.stdout.write
from string import digits as _digits_set

def polynomial_parse(_input_expression):
    _expression = _input_expression + "$"
    _cursor = 0

    def _parse_expression():
        nonlocal _cursor
        _terms = []
        _current_operator = '+'
        while True:
            _factor_terms = _parse_factor()
            if _current_operator == '-':
                for _term in _factor_terms:
                    _term[0] *= -1
            _terms.extend(_factor_terms)
            if _expression[_cursor] not in '+-':
                break
            _current_operator = _expression[_cursor]
            _cursor += 1
        _combined_terms = []
        for _k, _vars in _terms:
            for _cterm in _combined_terms:
                if _vars == _cterm[1]:
                    _cterm[0] += _k
                    break
            else:
                _combined_terms.append([_k, _vars])
        _filtered_sorted_terms = list(filter(lambda _t: _t[0] != 0, _combined_terms))
        _filtered_sorted_terms.sort()
        return _filtered_sorted_terms

    def _parse_factor():
        nonlocal _cursor
        _current_terms = [[1, []]]
        while True:
            _next_terms = _parse_ident()
            _new_terms = []
            for _coeff1, _vars1 in _current_terms:
                for _coeff2, _vars2 in _next_terms:
                    _var_map = {}
                    for _varname, _exp in _vars1:
                        _var_map[_varname] = _var_map.get(_varname, 0) + _exp
                    for _varname, _exp in _vars2:
                        _var_map[_varname] = _var_map.get(_varname, 0) + _exp
                    _combined_vars = list(_var_map.items())
                    _combined_vars.sort()
                    _new_terms.append([_coeff1 * _coeff2, _combined_vars])
            _current_terms = _new_terms
            while _expression[_cursor] == ' ':
                _cursor += 1
            if _expression[_cursor] in '+-$)':
                break
        return _current_terms

    def _parse_ident():
        nonlocal _cursor
        while _expression[_cursor] == ' ':
            _cursor += 1
        if _expression[_cursor] == '(':
            _cursor += 1
            _idval = _parse_expression()
            _cursor += 1
        elif _expression[_cursor] in _digits_set:
            _const_value = _parse_number()
            _idval = [[_const_value, []]]
        else:
            _var_name = _expression[_cursor]
            _cursor += 1
            while _expression[_cursor] == ' ':
                _cursor += 1
            if _expression[_cursor] == '^':
                _cursor += 1
                while _expression[_cursor] == ' ':
                    _cursor += 1
                _exponent_value = _parse_number()
            else:
                _exponent_value = 1
            _idval = [[1, [(_var_name, _exponent_value)]]]
        return _idval

    def _parse_number():
        nonlocal _cursor
        _num = 0
        while True:
            _ch = _expression[_cursor]
            if _ch not in _digits_set:
                break
            _num = 10 * _num + int(_ch)
            _cursor += 1
        return _num

    return _parse_expression()

def algebra_comparator_main():
    _first_input_line = _input_readline().strip()
    if _first_input_line == '.':
        return False
    _reference_polynomial = polynomial_parse(_first_input_line)
    while True:
        _next_input_line = _input_readline().strip()
        if _next_input_line == '.':
            break
        _comparison_polynomial = polynomial_parse(_next_input_line)
        _output_write("yes\n" if _reference_polynomial == _comparison_polynomial else "no\n")
    _output_write(".\n")
    return True

while algebra_comparator_main():
    pass