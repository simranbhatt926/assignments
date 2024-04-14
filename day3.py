# 1) create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.invoke caller function by passing show1,show2 and show3
     
def show1():
    print("This is show1.")

def show2():
    print("This is show2.")

def show3():
    print("This is show3.")

def caller(func):
    func()

caller(show1)
caller(show2)
caller(show3)




# 2) define nested function and show how will you invoke it.

def outer_function():
    print("This is the outer function.")

def inner_function():
    print("This is the inner function.")

print("Calling the inner function from within the outer function:")
inner_function()

outer_function()