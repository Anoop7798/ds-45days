import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)

#head()
df.head()

#head give by default 5 rows data
#if we want n rows than
print(df.head(2))
#-n is use to remove last n values and display other
print(df.head(-2))


#tail()
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
print(df.tail())

print(df.tail(-2))#skipc starting 2

print(df.tail(2))#give last two



#shape
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
print(df.shape)

#info
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df.info()

#verbose is use to print 

import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df.info(verbose=True)
#false means verbos ewill use to hide the info

import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df.info(verbose=False)

#null values
import pandas as pd
import numpy as np
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df["salary"]=[100,200,300,400,np.nan]
df.info()

#again shape
import pandas as pd
df=pd.DataFrame(data=[10,20,30,40,50])
print(df.shape)


#rename
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df1=df.rename(columns={"name":"student name"})
print(df)
print(df1)

#for original data rename
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df.rename(columns={"name":"student name"},inplace=True)
print(df)


#describe
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
df.marks.describe()
print(df)


#head
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
print(df.head())
print(df.head(2))
print(df.head(-2))

#tail
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
print(df.tail())
print(df.tail(2))
print(df.tail(-2))

#shape
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
print(df.shape)

#info
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
print(df.info())

#verbose
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
df.info(verbose=True)
df.info(verbose=False)
#false means verbos ewill use to hide the info


#rename
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
df.rename(columns={"Name":"student name"},inplace=True)
print(df)

#describe
import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)

df.Salary.describe()
print(df)



#add single column
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
#add single column data
df["name"]
#add single column
df["salary"]=df["marks"]+10
#add single column
df["salary"]=[100,200,300,400,500]
print(df)



import pandas as pd
d = {
    "name":["vishal","virat","vineet"], # 3 rows
    "salary":[100,200,300] # 3 rows
}
df = pd.DataFrame(data=d)
# df["marks"] = [10,20,30]
df["marks"] = df["salary"] / 2
print(df)

df["increment"]=df["salary"]/10+df["salary"]
print(df)

df.rename(columns={"increment":"salary inc"},inplace=True)
print(df)