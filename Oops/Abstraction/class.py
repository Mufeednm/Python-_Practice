from abc import ABC, abstractmethod

class Grand(ABC):
    @abstractmethod
    def a(self):
        pass

class Parent(Grand):
    def a(self,name):
        self.name=name
        print(f"its me {self.name}") 
        print(type())
    def b(self):
        print("from parent") 

# obj = Grand()  # This will raise TypeError since Grand is an abstract class
obj = Parent()
obj.a("mufeed")
# print(type(obj.a))
# obj.a()
