# __main__
#     __main__ is the name of the top-level environment where your program starts executing.

# if __name__ == "__main__":
#     It acts as a code guard to prevent specific blocks of code from running unexpectedly.
#     If you write function call at global level and you import the file in other file that function automatically called
#       so you need to guard that code using above statement
    
#     How it works: Before running your file, Python automatically creates a special hidden variable called __name__.
#     Running directly: 
#       python myscript.py => Python assigns the string "__main__" to __name__.
#     Importing: If you import your file inside another script (import myscript), Python assigns the actual file name "myscript" to __name__

# // calculate.py
def calculate_total(price, tax):
    return price + (price * tax)

# This block only runs if you run THIS file directly
# If another script imports your file this block are safely skipped.
if __name__ == "__main__":
    print("Executing script directly...")
    result = calculate_total(100, 0.05)
    print(f"Total Price: {result}")

# //main.py
calculate_total(100,10)

# __main__ is also used as a specialized filename within Python packages (folders containing multiple modules).

# python -m my_package_folder
    # If you place a file explicitly named __main__.py inside a package folder, 
    # Python treats it as the package's command-line entry point. 
    # It allows a user to execute the entire directory as a script via the -m flag

