def gen(l):
    counter=0
    while True:
        yield l[counter%(len(l))]
        counter+=1

a=gen([1,2,3,4])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
