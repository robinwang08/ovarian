import sys
from scipy.stats import binom_test

x = 0.96
n = 48
p = 0.78

print(binom_test(int(x * n), n, p))
