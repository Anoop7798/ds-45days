import matplotlib.pyplot as plt
x=[2015,2020,2025,2030]
y=[100,150,200,230]
plt.plot(x,y)#line graph
plt.ylabel("sales")
plt.xlabel("years")
plt.title("sales report")
plt.show() #graph show


import matplotlib.pyplot as plt
import numpy as np 
x =np.array([1,2,3,4])
y1=[10,20,30,40]
y2=[20,30,25,50]
y3=[10,20,25,40]
w=0.30
plt.bar(x - w,y1,label='boys',width=w)
plt.bar(x,y2,label='trans',width=w)
plt.bar(x + w,y3,label='girls',width=w)
plt.xlabel("groups")
plt.ylabel("number of student")
plt.title("number of student in each group")
plt.legend()
plt.show()



#histogram
import matplotlib.pyplot as plt
marks=[40,55,60,70,76,90,34,50]
plt.hist(marks,bins=4,orientation='vertical')
plt.show()

#pie chart
import matplotlib.pyplot as plt
fruits=['apple','banana','orange','watermelon']
count=[40,30,15,70]
x=['red','yellow','orange','green']
plt.pie(count,labels=fruits,colors=x)
plt.show()



import matplotlib.pyplot as plt
fruits=['apple','banana','orange','watermelon']
count=[40,30,15,70]
x=['red','yellow','orange','green']
plt.pie(count,labels=fruits,colors=x,startangle=90,autopct='%1.1f%%')
plt.show()


#subplot
import matplotlib.pyplot as plt
#first chart
plt.subplot(1,2,1)#row,col,position
x=[1,2,3,4]
y=[10,20,30,50]
plt.plot(x,y)
plt.xlabel("1x")
plt.ylabel("1y")
#second chart
plt.subplot(1,2,2)
fruits=['apple','banana','orange','watermelon']
count=[40,30,15,70]
plt.pie(count,labels=fruits,startangle=90)

plt.tight_layout()
plt.show()





import matplotlib.pyplot as plt
import numpy as np
 
plt.figure(figsize=(12,8))
 
# 1. Line Chart
plt.subplot(2,2,1)
 
x = [1,2,3,4,5]
y = [10,20,30,40,50]
 
plt.plot(x,y)
plt.title("Line Chart")
 
 
# 2. Bar Chart
plt.subplot(2,2,2)
 
x = ["A","B","C","D"]
y = [20,35,25,40]
 
plt.bar(x,y)
plt.title("Bar Chart")
 
 
# 3. Pie Chart
plt.subplot(2,2,3)
 
fruits = ["Apple","Banana","Orange","Mango"]
sales = [30,20,25,25]
 
plt.pie(sales, labels=fruits, autopct="%1.1f%%")
plt.title("Pie Chart")
 
 
# 4. Histogram
plt.subplot(2,2,4)
 
data = [10,12,15,18,20,22,25,28,30,35,40,45]
 
plt.hist(data, bins=3)
plt.title("Histogram")
 
plt.tight_layout()
plt.show()