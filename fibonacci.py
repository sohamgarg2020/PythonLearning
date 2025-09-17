def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    val = {0: 0, 1: 1}
    for i in range(2, n+1):
        val[i] = val[i-1]+val[i-2]
    return val[n]

def f(n):
    dp = [0]*(n+1)
    dp[1] = 1

    for x in range(2, n+1):
        dp[x] = dp[x-1]+dp[x-2]
    return dp[n]

def recfib(n):
    if n == 0: return 0
    if n == 1: return 1
    return recfib(n-1)+recfib(n-2)

def opfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev, cur = 0, 1

    for x in range(2, n+1):
        prev, cur = cur, prev+cur
    return cur

x = int(input("number: "))

print(f(x))
print(fib(x))
print(opfib(x))