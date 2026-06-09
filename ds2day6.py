class address:
# city="jaipur"
 #   district="meghalaya"
  #  state="rajasthan"
    def __init__(self,city,state):
        self.city=city
        self.state=state
        
a=address("jaipur","rajasthan")
#print(a.city)
#print(a.district)
print(a.state)

#class method and self
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
        
    def show(self):
        print("the city is:",self.city)
a=address("jaipur","rajasthan")
a.show()

#inheritance 
class address:
    def __init__(self,city,state):
     self.city=city
     self.state=state 
    def location(self):
      return f"my location is {self.city} in {self.state}"

class user(address):
    def __init__(self,name,age,city,state):
        self.name=name
        self.age=age
        self.city=city
        self.state=state
        
    def username(self):
        print(f"my name is {self.name}")
    def userdetails(self):
        print(f"my name is {self.name} and my location is {self.city} in {self.state}")
u=user("Anup",20,"kukas","rajasthan")
print(u.city)
u.location()
u.username()

u.userdetails()
a=address("kukas","rajasthan")




#encapsulation
class address:
    def __init__(self,city,state):
        self.__city=city#private attribute
        self.state=state
    def location(self):
        print(f"my location is {self.__city} in {self.state}")
    def get_city(self):
        return self.__city
a=address("chappra","bihar")
a.location()
a.get_city()
#print(a.__city)
print(a.state)

#polymorphism
class address:
  def __init__(self,city,state):
    self.city = city
    self.state = state
  def location(self):
    print(f"my address location is {self.city} in {self.state}")
 
class HomeTown:
  def __init__(self,city,state):
    self.city = city
    self.state = state
 
  def location(self):
    print(f"my home town location is {self.city} in {self.state}")
a=address("mahendergarh","haryana")
a.location()
b=HomeTown("narnaul","haryana")
b.location()

#class variable
class Withdraw:
  total = 0 # class variable
  def __init__(self,city,state):
    self.city = city
    self.state = state
    Withdraw.total += 1
 
  def location(self):
    print("location")
 
a = Withdraw("jaipur","rajasthan")
 
b = Withdraw("bhilwara","rajasthan")
 
a.total


#overloading and overriding

def address(city,state):
    print(f"my address is {city} in {state}")
def address(city,state,country):
    print(f"my address is {city} at {state} in {country}")
address("jaipr","rajasthan")
address("jai","rajasthan","india")



#overriding
class address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def location(self):
        print("address")
class user(address):
    def __init__(self,name,age,city,state):
        self.name=name
        self.age=age
    def location(self):
        print("user location")
u=user("arya",20,"kukas","rajasthan")
u.location()

#if we make super key than address or upper will be print 


#tuples
t=(10,20,30)
print(t[0])
print(t[-1])
#example
marks=[98,90,95,94]
marks[3]=50
print(marks)
print(type(marks))

#tuple cannot change the marks but the list can change or modify
marks=[98,90,95,94]
t=tuple(marks)
print(type(t))
print(t)
t[3]=55