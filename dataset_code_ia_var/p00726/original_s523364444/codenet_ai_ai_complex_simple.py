from functools import reduce
import operator
import itertools

uncompress = (lambda f: (lambda text, L, _call=None: f(text, L, _call or (lambda txt, l: uncompress(txt, l)))))(

    lambda text, L, _call: reduce(
        lambda acc, _: acc if len(acc[0]) > L else (
            lambda pos, newText: (
                (lambda c: (
                    (lambda endDigit=next(itertools.dropwhile(lambda i: text[i].isdigit(), range(pos, len(text)+1)), pos): (
                        (lambda t=text[pos:endDigit], nd=endDigit,
                                par=text[endDigit] if endDigit < len(text) else '', 
                                num=int(text[pos:endDigit]): (
                            (lambda endPar=(lambda ct, idx: next(i for i, ch in enumerate(text[nd:], nd) 
                                                                    if (ct := ct+1 if ch == '(' else ct-1 if ch == ')' else ct) == 0)
                                     )(1, nd)) : (
                                (
                                    lambda insideText=_call(text[nd+1:endPar-1], L-len(newText)): (
                                        lambda rep=''.join(itertools.islice(itertools.repeat(insideText, num), 
                                                                             max(0, (L-len(newText))//len(insideText)+2))): (
                                            (newText + rep[:max(0,L-len(newText)+1)], endPar)
                                        )
                                    )()
                                )
                            ),
                            (newText + text[nd]*num, nd+1)
                        )[0] if par != '(' else (newText + text[nd]*num, nd+1)
                        if par else (newText, nd)
                    ))()
                ))(text[pos]) if pos < len(text) else (newText, pos)
            ))(acc[1], acc[0])[::-1],
        itertools.count(0),
        ('', 0)
    )[0]
)

getEndParenthesis = lambda text, pos: next(
    i+1
    for i, c in enumerate(text[pos:], pos)
    if reduce(lambda acc, x: acc + (1 if text[x]=='(' else -1 if text[x]==')' else 0),
              range(pos,i+1), 0) == 0
)

getEndDigit = lambda text, pos: next(
    (i for i in range(pos, len(text)+1) if not (i<len(text) and text[i].isdigit())), pos
)

if __name__ == '__main__':
    ab, idx = '', ''
    import sys
    for line in sys.stdin:
        ab, idx = line.strip().split()
        if ab == '0' and idx == '0':
            break
        decompressed = uncompress(ab, int(idx))
        print(decompressed[int(idx)] if len(decompressed) > int(idx) else 0)