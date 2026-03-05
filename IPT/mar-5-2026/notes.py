# Function 
# --> block of statements that does a specific task

# syntax:
# def function_name parameter 
# FUNCTION PROTOTYPE: 
# first part = returning data type 
# second part: funtion name
# third part: parameter  >> formal parameter
# terminated by semi colon (;) 
# ex: int main ();

# FUNCTIONS TYPE
# --> user define 
# --> pre define

# FUNCTION DEFNITION 
# Function Heading
# Function Body
# Parameter >> actual parameter

# FUNCTION CALL 
# Parameter Passing: Formal PArameter replaced by Actual Parameter  

# Why we need to use function:
# --> To make our code modularized

# 1. Code Reusability  >> func can be use again and again 
# 2. Modularity  >> like chunking, fitting func anywhere in the code structure 
# 3. Readability  >> 
# 4. Maintainability >> 

def evenOdd(x):
    if (x % 2 == 0): 
        return "Even"
    else: 
        return "Odd"
    
print(evenOdd(12))
print(evenOdd(7))

# DEFAULT ARGUMENTS
def myFun(x, y=50): #default argument: y 
    print("x: ", x) 
    print("y: ", y)
myFun(10)

# KEYWORD ARGUMENTS
def student (fname, lname): 
    print(fname, lname)

student(fname = 'Lawrence', 
        lname='Panes')
student(lname='Panes',
        fname='Lawrence') # the order of the keyword doesnt matter 

# POSITIONAL ARGUMENTS
def nameAge (name, age): 
    print("Hi, I am ", name)
    print("My age is ", age)
print ("Case-1")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

# ARBITRARY ARGUMENTS
def myRun(*arg, **kwargs):
    print("Non-Keyword Arguments(*args):")
    for arg in args: 
        print(arg)
    print("\Keyword Arguments(**kwargs):")
    for key, value in kwargs.item(): 
        print (f"{key} == {value}")

myRun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')
# get the heart, get the bottom, go deeper 



