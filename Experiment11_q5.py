import pandas as pd
import numpy as np

# Create dictionary
exam_data = {
    'name': ['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
    'score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
    'attempts': [1,3,2,3,2,3,1,1,2,1],
    'qualify': ['yes','no','yes','no','no','yes','yes','no','no','yes']
}

# Define row labels
labels = ['a','b','c','d','e','f','g','h','i','j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Display first 3 rows
print("First three rows of DataFrame:\n")
print(df.head(3))   # head(3) returns first 3 rows