#pandas (numpy se hi bna h)
import pandas as pd
df = pd.Series([10,20,30])
print(df)
print(df[0])



import pandas as pd
dict ={"name":["hello","dheeraj","kunal","praveen","anjali","abhishek"],
       "age":[20,21,22,23,24,25],
       "salary":[15000,20000,25000,30000,35000,90000]
       }
df = pd.DataFrame(dict)
print(df)

#dict
import pandas as pd
dict = {"name":["dheeraj","kunal","praveen","anjali","abhishek singh"],
        "age":[20,21,22,23,30],
        "salary":[15000,20000,25000,30000,35000]
        }
df = pd.DataFrame(dict)
print(df)


#csv-> .csv(mainly common to excel without line)
#excel-> .xlsx
#json->.json


import pandas as pd
df = pd.read_csv("file1.csv")
print(df)


import pandas as pd
df = pd.read_json("file1.json")
print(df)


import pandas as pd
df = pd.read_excel("file1excel.xlsx")
print(df)
