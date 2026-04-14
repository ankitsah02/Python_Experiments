import pandas as pd
import numpy as np

# Create data with missing values (NaN)
data = {'A':[1,2,np.nan,4],
        'B':[5,np.nan,np.nan,8]}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display original data
print("Before replacing:\n", df)

# Replace missing values (NaN) with 0
df.fillna(0, inplace=True)

# Display updated data
print("After replacing:\n", df)