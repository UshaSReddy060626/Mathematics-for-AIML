import numpy as np
import matplotlib.pyplot as plt
population = np.random.randint(1, 101, 10000)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))
print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
plt.hist(sample_means, bins=30, edgecolor="black")
plt.title("Central Limit Theorem")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()