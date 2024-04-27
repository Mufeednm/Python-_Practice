#        public
# class a : 
#     def __init__(self,name):
#         self.name=name
#     def aa (self):
#         print (f"my name is {self.name}")
# nam=a("mufeed")
# print(nam.name)        
# nam.aa()        
#     protected
# class a : 
#     def __init__(self,name):
#         self._name=name
#     def aa (self):
#         print (f"my name is {self._name}")
# class b ():
#     def bb():
#         pass        
# nam=a("mufeed")
# print(nam._name)        
# nam.aa()     
#    private
class a : 
    def __init__(self,name):
        self.__name=name
    def aa (self):
        print (f"my name is {self.name}")
nam=a("mufeed")
print(nam.__name)        
nam.aa()     