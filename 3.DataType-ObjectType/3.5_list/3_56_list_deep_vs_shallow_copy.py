# Shallow Copy: A shallow copy creates a new object but inserts references to the objects found in the original.
# Deep Copy: A deep copy creates a new object and recursively copies all objects found within the original.

# copy() vs =(reference)
#   = would not actually create a copy of our list. The assignment operator would only create a reference to our list. 
#   original_list and reference_to_original_list refer to the same list after our assignment.
original_list = [[1,2], 2, 3]
reference_to_original_list = original_list
reference_to_original_list[0][0] = 99

print(original_list)                #  [[99,2],2,3]
print(reference_to_original_list)   #  [[99,2],2,3]

# --------------------------------------

# shallow copy:

# 1. a.using copy() (python 3.3+)
#    b. using copy.copy() same behaviour works with custom object type (generic way) 
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list[0] = 99

print(original_list)        # [1,2,3]

# 2. using list() constructor
original_list = [1, 2, 3]
copied_list = list(original_list)
copied_list[0] = 99

print(original_list)        # [1,2,3]

# 3. using slicing[:]
original_list = [1, 2, 3]
copied_list = original_list[:]
copied_list[0] = 99

print(original_list)        # [1,2,3]

# ---------------------------------------------------
import copy
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 99

print(original_list)        # [1,2,[3,4]]