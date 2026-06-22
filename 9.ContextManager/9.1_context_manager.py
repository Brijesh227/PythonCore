# context manager: https://chatgpt.com/share/6a38cbcf-90c4-83ee-900c-22615c021723

# need of context manager:

file = open("data.txt")
data = file.read()
1 / 0
file.close()        # never executes

# problem: I need to guarantee cleanup code runs even if an exception happens. if not then
#   File descriptor leaks
#   Database connections not released
#   Network sockets not closed
#   Locks never released

# solution:

# old approach:
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()

# problem with try and finally: 
#   it will create nested try/finally, not easy to read
conn = create_db_connection()
try:
    cursor = conn.cursor()
    try:
        process_data()
    finally:
        cursor.close()
finally:
    conn.close()

# context manager: (final solution)

with open("data.txt") as file:
    data = file.read()          # file close automatically

# internal work:

manager = open("data.txt")
file = manager.__enter__()
try:
    data = file.read()
finally:
    manager.__exit__()

# custom context manager
class Demo:
    def __enter__(self):
        print("Entering")
        return "hello"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

# usage:
with Demo() as value:
    print(value)    # Entering
                    # hello
                    # Exiting

# Demo()
#    ↓
# __enter__()
#    ↓
# value = return value
#    ↓
# with block executes
#    ↓
# __exit__()
