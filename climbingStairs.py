# Key takeaway: put the cache outside the function definitions to maintain
# a single variable that gets continuously updated

cache = {}

def fib(n):
    if n == 0: return 0
    if n == 1: return 1    
    
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    
    return cache[n]

def climbingStairs(n):
    return fib(n + 1)


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(6)) # 8
print("########")
print(climbingStairs(1)) # 1
print(climbingStairs(2)) # 2
print(climbingStairs(3)) # 3
print(climbingStairs(4)) # 5
print(climbingStairs(5)) # 8
print(climbingStairs(6)) # 13
print(climbingStairs(7)) # 21
print(climbingStairs(38)) # 63245986
