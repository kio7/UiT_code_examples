actual_weight = 78.56
zns = [78.2, 78.9, 78.1, 78.3, 78.4, 78.9, 78.6, 78.8, 78.7, 78.4, 79, 78.2, 78.7, 78.7, 78.3]
estimates = [zns[0]]

def new_estimate(new_pos, n):
    return estimates[-1] + 1/n*(new_pos - estimates[-1])

for i in range(1, len(zns)):
    estimates.append(new_estimate(zns[i], i))

# import matplotlib.pyplot as plt

# plt.plot(zns, label = 'Measurements')
# plt.plot(estimates, label = 'Estimates')
# plt.axhline(actual_weight, color = 'green' ,label = 'Actual weight')
# plt.legend()
# plt.xlabel('Attempt number')
# plt.ylabel('Weight')



# Oppgave 2

import os

file_dir = os.path.dirname(__file__)
lis = []

with open(os.path.join(file_dir, "noisy_position.txt"), "r") as file:
    file.readline() # First line is name of measurements and not actual measurements.
    for line in file:
        lis.append(line.strip().split("    "))

for elm in lis:
    elm[0] = float(elm[0])
    elm[1] = float(elm[1])


estimated_v = [0]
estimated_pos = [lis[0][1]]
alpha = 0.01
beta = 0.02

for zn in lis[1:]:
    e_v = estimated_v[-1] + beta*((zn[1] - estimated_v[-1])/0.5)
    e_pos = estimated_pos[-1] + alpha*(zn[1] - estimated_pos[-1])
    estimated_v.append(e_v)
    estimated_pos.append(e_pos)

# And plot... 