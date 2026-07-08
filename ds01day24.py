#decision tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_absolute_error

#data set
data={
    "age":[20,22,25,28,30,35,40,45,50,55],
    "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,90000],
    "buy":[0,0,0,0,1,1,1,1,1,0]
}

df=pd.DataFrame(data)
print(df)

#features and target
x=df[['age','salary']]#features
y=df['buy']#target

#train test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#model
model=DecisionTreeClassifier(random_state=42)
model.fit(x_train,y_train)
 
# prediction
 
y_pred = model.predict(x_test)
print("actual data",y_test)
print("prediction",y_pred)
 
 
 # random forest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # model accura
 
data = {
    "age":[20,22,25,28,30,35,40,45,50,55],
    "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
    "buy":[0,0,0,0,1,1,1,1,1,0]
}
 
df = pd.DataFrame(data)
print(df)
 
# x,y split
x = df[['age','salary']]
y = df['buy']
 
# train split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 
# model
model = RandomForestClassifier(random_state=42,n_estimators=10) # n_estimators
model.fit(x_train,y_train)
 
# prediction
y_pred = model.predict(x_test)
 
print("prediction")
print(y_pred)
print("acutal data")
print(y_test)
print("accuracy")
print(accuracy_score(y_test,y_pred))

import matplotlib.pyplot as plt
buy = df[df['buy'] == 1]
not_buy = df[df['buy'] == 0]

plt.scatter(buy['age'], buy['salary'], color='green', label='Buy')

plt.scatter(not_buy['age'], not_buy['salary'],color='red', label='Not Buy')

plt.title("Decision Tree / Random Forest Dataset")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()

from sklearn.metrics import confusion_matrix
 
actual = [1,0,1,1,0,1,0,0]
pred = [1,0,1,0,0,1,1,0]
 
cm = confusion_matrix(actual,pred)
print(cm)

# confusion metrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
 
actual = [1,0,1,1,0,1,0,0]
pred = [1,0,1,0,0,1,1,0]
 
ConfusionMatrixDisplay.from_predictions(actual,pred)
plt.show()



#presion| recall|f1 score 
import pandas as pd
import sklearn.metrics as metrics 
from sklearn.metrics import precision_score, recall_score, f1_score,confusion_matrix
actual = [1,0,1,1,0,1,0,0] 
predicted = [1,0,1,0,0,1,1,0] 
cm = confusion_matrix(actual,predicted) 
print("confusion matrix:\n",cm) 
print("Precision:",cm[1,1] / (cm[1,1] + cm[0,1])) 
print(3/(3+1)) 
precision  = precision_score(actual,predicted) 
print("Precision_Score:", precision) 
print("Recall:",(cm[1,1] / (cm[1,1] + cm[1,0])))

# recall 

print("recall",cm[0][0]/(cm[1][0]+cm[1][1]))

recall=recall_score(actual,predicted)

print("recall",recall)
 
# f1 score

f1Score=f1_score(actual,predicted)

print("f1_Score",f1Score)

print("f1_Score",(precision+recall)/2)

print("f1_Score",((cm[0][0]/(cm[0][0]+cm[1][0]))+(cm[0][0]/(cm[1][0]+cm[1][1])))/2)
 