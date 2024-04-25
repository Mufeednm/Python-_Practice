class parent1:
    
    def box (self,Box_name,num):
        self.box_name="mufeed"
        print(f"first boss name {Box_name},num={num}") 
class parent2 :
    def box2(self,box_name,num):
        print (f"sexond box name {box_name} nom = {num} ")
class child (parent1,parent2):
    def child(self,names):
        
        print(f"i am the child my parents name is {parent1.Box_name}")      
               

name=child()





