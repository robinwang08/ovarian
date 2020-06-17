import sys
from scipy.stats import binom_test

x = 0.6375
n = 53
p = 0.7725

#print(binom_test(int(x * n), n, p))
print(binom_test(int(53*.86), 53, 0.92))



