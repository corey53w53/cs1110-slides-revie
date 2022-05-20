class A():
    x = 1
    def __init__(self, n):
        self.y = n
        A.x += 1
    def p(self):
        print(self.y)
        self.y += 3
        self.r()
class B(A):
    x = 10
    def __init__(self, n):
        super().__init__(n)
        sum = self.y + B.x
        self.m = sum
    def r(self):
        self.y += self.x
        print(self.m)
b = B(2)
b.p()