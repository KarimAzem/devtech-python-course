# Create a function

def my_function():
    print("hi from the function")
    

# call a function 

# my_function()


def my_function_argument(name):
    print("hi" + name)
    
    
def my_function_multi_argument(fname, lname):
    print("hi " + fname + " " + lname)
# my_function_multi_argument(lname='last name', fname='first name')

def my_function_arg_num_aknown(*names):
    print(names[2])
    print(type(names))
#my_print(f"{chances} left ! ")function_arg_num_aknown('ahmed', 'karim', 'haitham')
    

def keyword_function(**names):
    print("your name is : " + names["first"])

#keyword_function(first = "karim", second = "haithem" )


def default_parametre_function(name="karim"):
    print(name)    
    
default_parametre_function("haithem")

names_list = ["karim", "khaled", "ahmed"]

def list_funciton(names):
    for i in names:
        print(i)
        
#list_funciton(names_list) 



# return function == return value

def function_return(a, b):
    return a+b


# pass
def empty_func():
    pass
 
# recursion  a function can call itself in itself     



# lambda 
# ? take many args but do one thing

x = lambda fname, lname : print(f"{lname}{fname}")

# x("l", "h")

def function_lambda(n):
    return lambda a : a**n


x = function_lambda(2)

# print(x(5))


