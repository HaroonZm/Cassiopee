__import__("functools").reduce(lambda _, __: globals().__setitem('S', globals().get('S', '') + "ACL") or None, range((lambda X: int(X.strip()))(input())), None)
print(globals()['S'])