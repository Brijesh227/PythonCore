# contextlib:
#   Modern way to write context manager class
#   Why do I need an entire class just for setup and cleanup?

# Evolution:
# try/finally
#     ↓
# Context Manager
# (__enter__/__exit__)
#     ↓
# with statement
#     ↓
# contextlib
# (@contextmanager)

class TempFile:
    def __enter__(self):
        print("Create file")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Delete file")

# contextlib
from contextlib import contextmanager

@contextmanager
def temp_file():
    print("Create file")

    try:
        yield
    finally:
        print("Delete file")

# before yield goes into __enter__(), after yield goes into __exit__()