# program crashes without try...except

def main():
    print("start")
    hello()
    print("end")
    
def hello():
    a = 0;
    print(a)
    n = calculate(a)
    print(n)
    
def calculate(n):
    num = 100 / n
    return num
        
main()

# start
# 0
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 16, in <module>
#   File "<main.py>", line 3, in main
#   File "<main.py>", line 9, in hello
#   File "<main.py>", line 13, in calculate
# ZeroDivisionError: division by zero

# -------------------
# try...except handle error in controlled way, code doesn't stop unexpectedly

def main():
    print("start")
    hello()
    print("end")
    
def hello():
    a = 0
    print(a)
    n = calculate(a)
    print(n)
    
def calculate(n):
    try:
        num = 100 / n
        return num
    except ZeroDivisionError:
        print("zero divide")
    # except ZeroDivisionError as e:
    #     print("Print Error", e)             # Print Error division by zero (e prints message not type, for type => type(e).__name__)
    # except ZeroDivisionError as e:
    #     raise "Error"                 # TypeError: exceptions must derive from BaseException                     
        
main()

# start
# 0
# zero divide
# None
# end

# if you raise it from any of the function code execution will stop

def main():
    print("start")
    hello()
    print("end")
    
def hello():            # if raise from here then and not from calculate then same behviour
    # try:
        a = 0;
        print(a)
        n = calculate(a)
        print(n)
    # except ZeroDivisionError as e:
    #     raise e
    
    
def calculate(n):
    try:
        num = 100 / n
        return num
    except ZeroDivisionError as e:
        raise e
        
main()

# start
# 0
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 20, in <module>
#   File "<main.py>", line 3, in main
#   File "<main.py>", line 9, in hello
#   File "<main.py>", line 18, in calculate
#   File "<main.py>", line 15, in calculate
# ZeroDivisionError: division by zero
