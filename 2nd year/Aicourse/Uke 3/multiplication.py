import time

num_1 = 3**150
num_2 = 2**100

start = time.perf_counter()

for i in range(1_000_000):
    num_1 / num_2

end = time.perf_counter()

print(end-start)