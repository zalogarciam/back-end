
def arg_function(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
  
  
arg_function('Hello', 'Welcome', 'to', 'my', 'app')

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
  
  
# Driver code
kwargs_function(first='Hello', mid='my', last='World')

def div(a, b):
    
    try:
        r = a/b
        return r
    except ZeroDivisionError: 
        return "Cannot divide by zero"
    except TypeError: 
        return "Please use numbers"
    except:
        return "Error"

print(div(10, 2))
print(div(10, 3))
 
