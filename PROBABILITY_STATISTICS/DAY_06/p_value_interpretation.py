from scipy import stats
scores = [72, 75, 70, 68, 74, 73, 71, 69]
t_stat, p_value = stats.ttest_1samp(scores, popmean=70)
print("t-statistic:", t_stat)
print("p-value:", p_value)
alpha = 0.05
if p_value < alpha:
    print("\nDecision: Reject the Null Hypothesis (H₀)")
    print("Conclusion: The average score is significantly different from 70.")
else:
    print("\nDecision: Fail to Reject the Null Hypothesis (H₀)")
    print("Conclusion: There is not enough evidence to say the average score is different from 70.")