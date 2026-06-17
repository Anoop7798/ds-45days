import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
 
#print(df)
df.loc[4, "marks"] =np.nan
df.loc[4, "marks"] = None
#print(df)
#print(df.isnull())
#print(df.isnull().sum())
#drop null values by row
#df.dropna(inplace=True)

#drop null values by column
#df.dropna(axis=1,inplace=True)


#fill by zeroes & 100
#df.fillna(100,inplace=True)

#rol->200,marks->100
#df.fillna({"roll no": 200, "marks": 100}, inplace=True)

mm=df['marks'].mean()
df['marks']=df['marks'].fillna(mm)
print(df)
print(df.isnull())
print(df.isnull().sum())



#AGGREGATION
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
#print(df)
#manually
print(df['marks'].sum())
print(df['marks'].mean())
print(df['marks'].min())
print(df['marks'].max())


#concatenate

import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df1=pd.read_json(url)

#pd.concat([df,df1])  #row

s=pd.concat([df,df1],axis=1)  #column

print(s) 
 
 
 
 # concatenate
import pandas as pd
url = "https://raw.githubusercontent.com/ajay2712006/ds45/main/file2.json"
df1 = pd. read_json (url)
df = pd. read_json (url)
# pd.concat([df,df1]) # row
df1.loc[2, "name"] = "Anoop"
s=pd.concat([df, df1], axis=1)

print(s)


#plot graph
import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score, over)
plt.show()