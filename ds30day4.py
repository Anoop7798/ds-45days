l=[10,20,30]
l.append(50)
print(l)


import math
print(math.factorial(5))


from math import factorial,pi

print(factorial(5))
print(pi)


import math as anup


#day-5(01/06/2026)
#oop concept
 #set & sets operations
 # example
class rajendra:
  def __init__(self,name):
    self.name = name
  def show(self):
    print(self.name)
 
r = rajendra("hello")
r.show()
 
 
class anup:
   def __init__(self,name):
        self.name=name
   def show(self):
      print(self.name)
            
r = anup("hello")
r.show()

class anup:
  def __init__(self):
   print("calling constructor")
  
  def show(self):
   print("show func clling")
     
r = anup()
r.show()

class anup:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getage(self):
        print("my age is:",self.age)
        
    def getname(self):
        print("my name is:",self.name)
        
r= anup("hello",20)
r.getage()
r.getname()



class student:
    def __init__(self,args):
        print(type(args))
        print(args)
        self.name = args
    def getstu(self):
        return self.name
    
s=student({"name":"helo","age":20})
t =s.getstu()
print(t["age"])


