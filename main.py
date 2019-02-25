def add(x,y):
    """Return the sum of x and y"""
    return x+y

def subtract(x,y):
    """Return the result of x minus y"""
    return x-y

def multiply(x,y):
    """Return the result of x multiplied by y"""
    return x*y

def divide(x,y):
    """Return the result of x divided by y"""
    return x/y

def calc():
    """Asks the user what to do"""
    while True:
        x = input("Please enter the first number: ")
        try:
            x = int(x)
            break
        except:
            print("Invalid entry\n")
    while True:
        y = input("Please enter the second number: ")
        try:
            y = int(y)
            break
        except:
            print("Invalid entry\n")
    while True:
        func = input("Please enter the function (a)dd, (s)ubtract, (m)ultiply, (d)ivide: ")
        if func == "a" or func == "add":
            return("{} plus {} is {}".format(x, y, add(x,y)))
        elif func == "s" or func == "subtract":
            return("{} minus {} is {}".format(x, y, subtract(x,y)))
        elif func == "m" or func == "multiply":
            return("{} times {} is {}".format(x, y, multiply(x,y)))
        elif func == "d" or func == "divide":
            return("{} divided by {} is {}".format(x, y, divide(x,y)))
        else: print("Invalid entry\n")

print(calc())