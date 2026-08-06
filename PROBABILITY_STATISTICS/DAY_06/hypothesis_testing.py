from scipy import stats
scores = [72,75,70,68,74,73,71,69]
t_stat, p_value = stats.ttest_1samp(scores, popmean=72)
print("t-statistic:", t_stat)
print("p-value:", p_value)