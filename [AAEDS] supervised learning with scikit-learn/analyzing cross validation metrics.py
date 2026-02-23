# Print the mean
import numpy as np
print(np.mean(cv_result))

# Print the standard deviation
print(np.std(cv_result))

# Print the 95% confidence interval
print(np.quantile(cv_result, [0.025, 0.975]))