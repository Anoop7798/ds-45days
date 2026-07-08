# handle missing values
import pandas as pd
import numpy as np
data = {
    "colors":['red','green','blue','orange','green','blue',np.nan]
}
df = pd.DataFrame(data)
print(df)
 

# handle null values
df.dropna(inplace=True)
print(df)