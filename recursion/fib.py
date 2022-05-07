memo={}
def fib(n):
    if n<=2: return 1
    elif n in memo.keys(): return memo[n]
    else:
        answer=fib(n-1)+fib(n-2)
        memo[n]=answer
        return answer
print(fib(100))