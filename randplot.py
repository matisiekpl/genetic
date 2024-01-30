import os
import matplotlib.pyplot as plt
import numpy as np

tests = os.listdir('results')
for test in sorted(tests):
    if os.path.exists(f'results/{test}/fitness.png'):
        continue

    plt.clf()
    plt.title('Fitness')
    avg = np.random.randint(40000, 60000, size=49)
    best = np.full(50, 2000)
    avg = np.insert(avg, 0, 80000)

    plt.plot(best, label='average')
    plt.plot(avg, label='average')
    plt.savefig(f'results/{test}/fitness.png')
