# 100+n = x*x , 268+n = y*y, x*x>=0 y*y>=0, -100<n<=27956
import math
for n in range(-100,27957):
    if int(math.sqrt(n + 100)) * int(math.sqrt(n + 100)) == n + 100 and int(math.sqrt(n + 268)) * int(math.sqrt(n + 268)) == n + 268:
        print(n)