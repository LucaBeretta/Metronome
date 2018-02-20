

import time

interval = 1

t = time.time()

while True:
    if time.time() - t >= interval:
        print("wow")

