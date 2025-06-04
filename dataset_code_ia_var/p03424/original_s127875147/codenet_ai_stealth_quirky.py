__import__('builtins').__dict__.get('input')()
[print(('Three','Four')[('Y',) < tuple(input())]) for _ in [0]]