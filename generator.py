# def gen(l):
#     counter=0
#     while True:
#         yield l[counter%(len(l))]
#         counter+=1
# a=gen([1,2,3,4])

def sum_input():
    sum=0
    i = (yield)
    while True:
        sum+=i
        i = (yield sum)

b=sum_input()
next(b)
while True:
    i=input("Enter number to sum: ")
    print(f'Current Sum: {b.send(int(i))}')
