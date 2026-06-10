#pandas continue 
#csv->comma separated values
#json->java script object notation
#excel->table form
import pandas as pd
from pandas import read_csv 
import pandas
from pandas import *


import pandas as pd
df = pd.Series([10,20,30])
print(df)



import pandas as pd
l=[10,20,30]
df = pd.Series(data=l)
print(df)

import pandas as pd
d={ "name":"kunal","age":"21","roll":123 }
df=pd.Series(data=d)
print(df)

#for data of series
import pandas as pd
help(pd.Series)


#dataframe
import pandas as pd
d={"name";"kunal","age":"21","roll":123}
df=pd.Series(data=d,index=)
print(df)


import pandas as pd
d={
    "name":["kunal","dheeraj","anjali","praveen","yash","danish"],
       "roll no":[12,13,14,15,16,17]
       }

df = pd.DataFrame(data = d)
print(df)

#csv
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2%20-%20Sheet1.csv"
df= pd.read_csv(url)
print(df)


#excel
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.xlsx"
df= pd.read_excel(url)
print(df)

#json
import pandas as pd
url="https://raw.githubusercontent.com/Anoop7798/ds-45days/main/file2.json"
df= pd.read_json(url)
print(df)

