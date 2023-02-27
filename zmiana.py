from textwrap import wrap
from collections import Counter
import random


def zmiana(res, string):

    lstr = [*string]
    result = []
    for i in lstr:
        possible = []
        chances = []
        for e in res[i]:
            possible.append(e["codon"])
            chances.append(e["i"] * 100)
        rand = random.choices(possible, weights=chances, k=1)
        result.append(rand[0])
    # print("".join(result))


    return result

