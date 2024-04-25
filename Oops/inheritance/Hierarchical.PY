class Parent :
    def __init__(self,A_name,age):
        self.name=A_name
        self.age=age
        
    def mom (self):
        print ("parent") 
        
class son (Parent):
    def child (self):
        print("son")    
            
class daughter (Parent):
    def childern (self,name,age ,names ):
        self.name=names
        print("son")        
class baby (Parent):
    def babys (self,name,age ,names ):
        self.name=names
        print("son")        
           
obj=baby("babus",52)
      
obj.mom()        