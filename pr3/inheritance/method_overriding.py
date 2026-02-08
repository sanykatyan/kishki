class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")




class Animal:
    def sound(self):
        print("...")

class Dog(Animal):
    def sound(self):
        print("woof")



class Base:
    def show(self):
        print("base")

class Child(Base):
    def show(self):
        print("child")
