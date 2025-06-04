print(
    max(
        [
            sum(
                map(
                    int,
                    input().split()
                )
            )
            for _ in range(
                int(
                    input().split()[0]
                )
            )
        ]
    )
)