import abc

class MyInterface(abc.ABC):
    @abc.abstractmethod
    def my_method(self):
        pass

class A(MyInterface):
    def __init__(self, name):
        self.name = name

    def my_method(self):
        return self.greet()

    def greet(self):
        return f"Hello, {self.name}!"

class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def my_method(self):
        return self.greet() + " !!! "

    def greet(self):
        return f"Hello, {self.name}! You are {self.age} years old."

if __name__ == "__main__":
    a = A("Alice")
    print(a.my_method())

    b = B("Bob", 30)
    print(b.my_method())

    if isinstance(a, A):
        print("a is an instance of class A")
    if isinstance(b, B):
        print("b is an instance of class B")
    if isinstance(b, A):
        print("b is also an instance of class A")
    if isinstance(a, B):
        print("a is an instance of class B")
    if isinstance(a, MyInterface):
        print("a implements MyInterface")
    if isinstance(b, MyInterface):
        print("b implements MyInterface")