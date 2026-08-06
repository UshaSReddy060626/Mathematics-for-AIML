import numpy as np
from scipy import stats
data = [65,70,75,80,85,90,95]
confidence = 0.95
mean = np.mean(data)
sem = stats.sem(data)
interval = stats.t.interval(confidence,
    len(data)-1,
    loc=mean,
    scale=sem)
print("Mean:", mean)
print("95% Confidence Interval:", interval)
