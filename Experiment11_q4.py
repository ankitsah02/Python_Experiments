import pandas as pd   # Import Pandas

# Create dictionary data
data = {'X':[78,85,96,80,86],
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original data
print("Original DataFrame:\n", df)

# Perform power operation (X raised to power Y)
power_result = df['X'] ** df['Y']

# Display result
print("X^Y values:\n", power_result)