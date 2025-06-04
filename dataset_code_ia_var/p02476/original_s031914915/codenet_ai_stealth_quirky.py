def _(_):return [int(__) for __ in _.split()]
f=lambda x,y:x%y
exec('aa,bb=_input_()\nprint(f(aa,bb))'.replace('_input_','_')(input))