from typing import List


def prime_factors(x: int) -> List[List[int]]:
    res = list()
    d = 2
    while x > 1:
        if x % d == 0:
            if len(res) == 0 or res[-1][0] != d:
                res.append([d, 1])
            else:
                res[-1][1] += 1
            x //= d
        else:
            d += 1

    return res
