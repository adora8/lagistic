import numpy as np
import time
# 向量化实现
a = np.random.rand(1000000)
b = np.random.rand(1000000)
tic = time.time()
c = np.dot(a, b)
toc = time.time()
print(c)
print("Vectorized version:"+str(1000*(toc-tic))+"ms")
# 非向量化实现
c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print(c)
print("For loop:"+str(1000*(toc-tic))+"ms")