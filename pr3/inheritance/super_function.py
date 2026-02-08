class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")



class Parent:
    def greet(self):
        print("hi")

class Child(Parent):
    def greet(self):
        super().greet()
        print("child")




class Base:
    def __init__(self, x):
        self.x = x

class Derived(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y



