actual_weight = 78.56
zns = [78.2, 78.9, 78.1, 78.3, 78.4, 78.9, 78.6, 78.8, 78.7, 78.4, 79, 78.2, 78.7, 78.7, 78.3]
estimates = []
alpha = 0.1 # This is changable, "amout of change"

def new_estimate(new_pos, n):
    return estimates[-1] + 1/n*(new_pos - estimates[-1])

for i in range(len(estimates)):
    estimates.append(new_estimate(zns[i], i))

print(estimates)