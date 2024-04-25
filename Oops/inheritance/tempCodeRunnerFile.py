class A:
    def m1(self,name):
        self.a=name
        
class B:
    def m2(self):
        pass
    
class   C(A,B):
    def m3(self):
        print(self.a)
        
obj=C()

obj.m1('hello')

obj.m3()