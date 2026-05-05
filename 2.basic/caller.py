from hello_python import greet

greet("caller")

# once you run this file it's create __pycache__ folder and create hello_python.cpython-312.pyc file.

# when you run python caller.py (https://www.youtube.com/watch?v=3HTKc-ZgZbg&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=3)

    # python interpreter will look for the bytecode file hello_python.cpython-312.pyc in __pycache__ folder and execute it instead of running hello_python.py file. This is because bytecode files are faster to execute than source code files. 
    # If the bytecode file is not found or is outdated, the interpreter will compile the source code file and create a new bytecode file before executing it.
    # Bytecode will generate everytime but it's visible when we import the module in __pycache__ folder.