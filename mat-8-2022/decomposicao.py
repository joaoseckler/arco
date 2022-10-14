from random import choice, randint
from functools import reduce
from operator import mul

# Esse script sorteia números fáceis de serem decompostos em fatores
# primos.

primos = [2, 3, 5, 7, 11, 13]
c = [choice(primos) for _ in range(randint(1, 7))]

print(c, "-", reduce(mul, c, 1))
