class Grand :
    def __int__(self):
        print("grandparent")
        
class parent (Grand) :
    def __int__(self):
        print("from parents")
        
class son (parent):
    def __int__(self):
        print("from son") 
                      
baby=son()
   