import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y=[100,120,230,300] #y coordinate

plt.plot(x,y)#line graph
plt.ylabel("sales")
plt.xlabel("years")
plt.title("sales report")
plt.show() #graph show



import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y=[100,120,230,300] #y coordinate
plt.plot(x,y)
plt.figure(figsize=(6,3))#width or height
plt.show()



import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y=[100,120,230,300] #y coordinate
plt.plot(x,y,color='green',marker='o',linestyle='dashed',linewidth=4,markersize=14)
plt.show()

# **Markers**
 
# |character      |  |  |description |
# |-------------|  -------------------------------|
# |'.'       | | |point marker|
# |','       | | |pixel marker|
# |'o'       | | |circle marker|
# |'v'       | | |triangle_down marker|
# |'^'       | | |triangle_up marker|
# |'<'       | | |triangle_left marker|
# |'>'       | | |triangle_right marker|
# |'1'       | | |tri_down marker|
# |'2'       | | |tri_up marker|
# |'3'       | | |tri_left marker|
# |'4'       | | |tri_right marker|
# |'8'       | | |octagon marker|
# |'s'       | | |square marker|
# |'p'       | | |pentagon marker|
# |'P'       | | |plus (filled) marker|
# |'*'       | | |star marker|
# |'h'       | | |hexagon1 marker|
# |'H'       | | |hexagon2 marker|
# |'+'       | | |plus marker|
# |'x'       | | |x marker|
# |'X'       | | |x (filled) marker|
# |'D'       | | |diamond marker|
# |'d'       | | |thin_diamond marker|
# |'|'       | | |vline marker|
# |'_'       | | |hline marker|
 
# **Line Styles**
 
# |character      |  |  |  |description |
# |-------------|   -------------------------------|
# |'-'       | | | |solid line style|
# |'--'      | | | |dashed line style|
# |'-.'      | | | |dash-dot line style|
# |':'       | | | |dotted line style|
 
# Example format strings:
 
#     'b'    # blue markers with default shape
#     'or'   # red circles
#     '-g'   # green solid line
#     '--'   # dashed line with default color
#     '^k:'  # black triangle_up markers connected by a dotted line
# **Colors**
 
# |character      |  |  |  |color |
# |-------------|   -------------------------------|
# |'b'       | | | |blue|
# |'g'       | | | |green|
# |'r'       | | | |red|
# |'c'       | | | |cyan|
# |'m'       | | | |magenta|
# |'y'       | | | |yellow|
# |'k'       | | | |black|
# |'w'       | | | |white|

#multiple line chart
import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y1=[100,120,230,300]
y2=[150,180,185,300]
plt.plot(x,y1,label='shirt')

plt.plot(x,y2,label='jeans')
plt.legend()
plt.show()






import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y1=[100,120,230,300]#y coordinate

y2=[150,180,185,300]
plt.plot(x,y1,label='jeans',color='green',marker='o',linestyle='dashed',linewidth=4,markersize=14)

plt.plot(x,y2,label='shirt',color='red',marker='o',linestyle='-',linewidth=2,markersize=10)

plt.ylabel("sales")
plt.xlabel("years")
plt.title("sales report")
plt.legend()
plt.show()




import matplotlib.pyplot as plt
 
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
 
y = [120, 150, 170, 160, 190, 220]
y1 = [100, 140, 180, 200, 210, 240]
 
plt.plot(x,y,color="green",marker="o",linewidth=2,label="Company A")
 
plt.plot(x,y1,color="purple",marker="s",linewidth=2,label="Company B")
 
plt.legend()
 
plt.show()


#bar chart
import matplotlib.pyplot as plt  #visualization
x=[2010,2015,2020,2025] #x coordinate
y=[100,120,230,300]#y coordinate
plt.bar(x,y)
plt.figure(figsize=(6,2))
plt.show()




import matplotlib.pyplot as plt
 
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
 
y = [120, 150, 170, 160, 190, 220]
y1 = [100, 140, 180, 200, 210, 240]
 
plt.bar(x,y,color="green",linewidth=2,label="Company A")
 
plt.bar(x,y1,color="purple",linewidth=2,label="Company B")
 
plt.legend()
 
plt.show()




import matplotlib.pyplot as plt
import numpy as np 
x =np.array([1,2,3,4])
y1=[10,20,30,40]
y2=[20,30,25,50]
w=0.40
plt.bar(x - w/2,y1,label='boys',width=w)#hide second
plt.bar(x + w/2,y2,label='girls',width=w)#show
plt.xlabel("groups")
plt.ylabel("number of student")
plt.title("number of student in each group")
plt.show()

