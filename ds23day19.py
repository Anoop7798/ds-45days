import pandas as pd
data={
    'Name':['ram','kamal','ajay'],
    'age':[25,None,32],
    'salary':[5000,6000,None]
}
df=pd.DataFrame(data)
print("original data")
print(df)

# Find null values
print("\nNull Values:")
print(df.isna())

# Count null values in each column
print("\nNull Count:")
print(df.isna().sum())

# Drop rows containing null values
print("\nAfter dropna():")
print(df.dropna())

# Fill null values
df_fill = df.fillna({
    'age': df['age'].mean(),
    'salary': df['salary'].mean()
})

print("\nAfter fillna():")
print(df_fill)


#encoding missing values
# encoding
from sklearn.preprocessing import LabelEncoder
import pandas as pd
 
data = {
    'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
    'Age':[25,None,32,20,21,22],
    'Salary':[5000,6000,None,7000,8000,9000],
    'Gender':['male','male','male',None,'female','female']
}
 
df = pd.DataFrame(data)
print("original dataframe")
print(df)

# label encoder
le = LabelEncoder()
df_label = df.copy()
df_label['Gender'] = df['Gender'].fillna('unknown')
df_label['Gender_encoder'] = le.fit_transform(df_label['Gender'])
 
print("After label encoding:")
print(df_label)
 
#one hot encoding
import pandas as pd
data = {
    'colors':['red','blue','green','red','blue']
}
 
df = pd.DataFrame(data)
print("original data")
print(df)
 
# one hot encoding
encoded_df = pd.get_dummies(df,columns=['colors'])
 
print("after one hot encoding")
print(encoded_df)
 