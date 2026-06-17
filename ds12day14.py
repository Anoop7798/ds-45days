#by default sorting is ascending 
#for descending pass ascending =false

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
#by default ascending
print(df.sort_values("english"))
#for descending
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df.sort_values("english",ascending=False))

#by arguement

import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df.sort_values(by=['english']))
#multiple columns
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df.sort_values(by=['english'],ascending=[False]))


import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df.sort_values(by=['english','maths'],ascending=[False,True]))




import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
#for upper case
df['name']=df['name'].str.upper()
print(df.sort_values('name'))


#add column
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
df['total']=df['english']=df['maths']+df['physics']
#print(df)


#add row
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
df.loc[14]=["anoop",'Male',80,90,100]
print(df)



#update column
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)



#update row
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)


#delete column
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
df1=df.drop("english",axis=1)
print(df1)


#delete row
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
df1=df.drop(13,axis=0)
print(df1)





#operation on row and columns
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df)
df.drop([6,7,8,9,10,11,12,13,14],inplace=True)
df
df['doj'] = ['2025-01-01','2025-02-02','2025-03-03','2025-04-04','2025-05-05','2025-06-06']
df
