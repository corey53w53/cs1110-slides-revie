def f(nlist):
    if nlist==[]: return []
    return f(nlist[1:]) if nlist[0]<0 else [nlist[0]]+f(nlist[1:])
print(f([1,-2,3,0,-5,6]))
