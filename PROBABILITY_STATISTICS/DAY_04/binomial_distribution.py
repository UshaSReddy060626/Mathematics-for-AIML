from scipy.stats import binom
n = 10
p = 0.5
print("Probability of exactly 6 successes:")
print(binom.pmf(6, n, p))
