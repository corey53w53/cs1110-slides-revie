class test(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("rann")

class child(test):
    def __init__(self,a,b,c):
        super().__init__(a+1)
        self.c=c
class grandchild(test):
    def __init__(self,a,b):
        super(child,child).__init__(a+2,b+2)

me=grandchild(3,4)
print(me.a)
print(me.b)