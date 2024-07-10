import random
import math 

N = 10000000
n = 0
for i in range(N):
    x = random.random()
    y = random.random()
    r = math.sqrt(x**2 + y**2)
    if r < 1:
        n += 1

print((4*n)/N)
