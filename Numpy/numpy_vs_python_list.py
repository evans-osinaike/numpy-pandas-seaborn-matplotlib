import time
import numpy as np

x = np.random.random(10000000)

# Using normal python for computation
start = time.time()
mean_x = sum(x)/len(x)
end = time.time()
print(end - start)

# Using numpy for computation
start = time.time()
mean_x = np.mean(x)
end = time.time()
print(end - start)
