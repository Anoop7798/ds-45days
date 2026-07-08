import pandas as pd
from sklearn.cluster import KMeans

data={
    "age":[22,25,24,45,50,40,20,47],
    "income":[22000,25000,24000,45000,50000,40000,20000,47000]
}
df=pd.DataFrame(data)
print(df)

#input \ feature
x=df[['age','income']]
#model
model=KMeans(n_clusters=2,random_state=42) #n_cluster ->2 mein divide krega
model.fit(x)

#cluster
clusters=model.labels_  #0 define younger and 1 defines older age
print(clusters)
df['cluster']=clusters  #add new columns
print(df)

#more example
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data={
    "age":[22,25,24,45,50,40,20,47],
    "income":[22000,25000,24000,45000,50000,40000,20000,47000]
}
df=pd.DataFrame(data)
print(df)

x=df[['age','income']]
model=KMeans(n_clusters=2,random_state=42)
model.fit(x)

df['cluster']=model.labels_
plt.scatter(df['age'],df['income'],c=df['cluster'])
plt.xlabel('age')
plt.ylabel('income')
plt.title('group of cluster datA')

plt.show()


#more example task
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data={
    "age":[22,25,24,45,50,40,20,47],
    "income":[22000,25000,24000,45000,50000,40000,20000,47000]
}
df=pd.DataFrame(data)
print(df)

x=df[['age','income']]
model=KMeans(n_clusters=2,random_state=42)
model.fit(x)

df['cluster']=model.labels_

#graph plotting
plt.plot(df['age'],df['income'])
plt.xlabel('age')
plt.ylabel('income')
plt.title('group of cluster datA')

plt.show()


#deep learning is a branch of Ml uses artificial neural network many layers to learn patterns from large amount of data
import tensorflow as tf
