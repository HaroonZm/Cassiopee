from functools import reduce
import operator

H,W=map(int,(lambda x:reduce(operator.add,map(list,x.split(" "))))(input()))

city=list(
    map(
        lambda r:
            list(
                map(
                    lambda t:
                        (lambda x,y: str(-1) if x<0 else str(x))(t,t),
                    reduce(
                        lambda acc,c:
                            acc[:-1]+[0] if c=="c" else acc+[acc[-1]+1] if acc else [1000],
                        r,
                        [-1000]
                    )[1:]
                )
            ),
        [input() for _ in range(H)]
    )
)

print("\n".join(map(lambda row:" ".join(row), city)))