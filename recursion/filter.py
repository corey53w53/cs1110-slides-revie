def f(l):
    if l==[]: return []
    return f(l[1:]) if l[0]<0 else [l[0]]+f(l[1:])
print(f([0,1,-3,4,-7,2]))