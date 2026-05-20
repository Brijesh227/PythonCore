# Types of Recursion
#       Recursion can be broadly classified into two types: 
#           tail recursion and non-tail recursion. 
#           The main difference between them is related to what happens after recursive call.

#           Tail Recursion: 
#               The recursive call is the last thing the function does, so nothing happens after it returns. 
#               Some languages can optimize this to work like a loop, saving memory.

#           Non-Tail Recursion: 
#               The function does more work after the recursive call returns, so it can’t be optimized into a loop.


# Example: This code compares tail recursion and non-tail recursion using two versions of factorial function one with an accumulator (tail-recursive) and one with multiplication after recursive call (non-tail-recursive).
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    if n == 0:
        return 1
    else:
        return n * nontail_fact(n-1)
        
print(tail_fact(5))  
print(nontail_fact(5))