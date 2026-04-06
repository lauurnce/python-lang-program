
def greeting(name):
  print("Hello, " + name)
  
import mymodule
mymodule.greeting("Jonathan") #Jonathan is argument 

#dictionary variable
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule
a = mymodule.person1["age"] # 'age' is a constant
print(a) #36 

# alias is object name
import mymodule as mx # 'mx' is the alias 

a = mx.person1["age"]
print(a)

import platform
x = platform.system() # 'system' is the name of the library or package 
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1

print (person1["age"])