from scipy.stats import bernoulli
p=0.8
print("Success:",bernoulli.pmf(1,p))
print("Failure:",bernoulli.pmf(0,p))
