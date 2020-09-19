import time
import math

print(format(1234, ","))

startTime = time.time()
time.sleep(2)
print(startTime)

time.sleep(1)
endTime = time.time()
start_time = endTime - startTime
print(int(start_time))
