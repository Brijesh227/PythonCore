# with is syntactic sugar of try..finally with __enter__ and __exit__
#   - it doesn't handle exception it forwards exception to __exit__() and context manager decides what to do, it __exit__() return True then exception suppressed.
#     
# context manager is simply setup + cleanup abstraction
# class Something:
#     def __enter__(self):
#         ...

#     def __exit__(self, exc_type, exc_value, traceback):
#         ...

# context manager: https://chatgpt.com/share/6a38cbcf-90c4-83ee-900c-22615c021723

# Need of context manager:

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
    # with something:
    #     ...

    # and expects:
    # something.__enter__()
    # something.__exit__()

manager = Demo()
value = manager.__enter__()

try:
    block()             # statement inside with block
except Exception:
    manager.__exit__(...)
    raise
else:
    manager.__exit__(None, None, None)

# custom context manager
class Demo:
    def __enter__(self):
        print("Entering")
        return "hello"

    def __exit__(self, exc_type, exc_value, traceback):     # if you retrun True exception suppress. 
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
# value = return value by __enter__ (variable used after as)
#    ↓
# with block executes
#    ↓
# __exit__()

# Context Manager  <-- used by --> with statement


# Multiple context manager:

with open("a.txt") as f1, open("b.txt") as f2:
    pass

# or

with open("a.txt") as f1:
    with open("b.txt") as f2:
        pass

# execution order
# f1.__enter__()
#        ↓
# f2.__enter__()
#        ↓
# block
#        ↓
# f2.__exit__()
#        ↓
# f1.__exit__()


# Any resource acquired before __enter__ completes successfully must be cleaned up by __enter__ itself if an exception occurs. 
# __exit__ is only guaranteed to run after a successful return from __enter__.

class Transaction:
    def __enter__(self):
        self.conn = connect_db()        # success
        self.conn.begin()               # failed due to some reason
        return self.conn
    
    def __exit__(self):
        self.conn.close()

    # improved __enter__

    def __enter__(self):
        self.conn = connect_db()

        try:
            self.conn.begin()
            return self.conn
        except:
            self.conn.close()
            raise

