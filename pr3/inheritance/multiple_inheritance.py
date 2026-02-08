class A:
    pass

class B:
    pass

class C(A, B):
    pass




class A:
    def f(self):
        print("A")

class B:
    def f(self):
        print("B")

class C(A, B):
    pass





class X:
    x = 1

class Y:
    y = 2

class Z(X, Y):
    pass
