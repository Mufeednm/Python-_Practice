# class Car_Design:
#     pass
# Suv=Car_Design()
# Sedan= Car_Design()
# print(type(Suv))
# print(type(Sedan))
#         adding detials or attributes
# class School:
#     def __init__(self,Name,age):
#         self.name=Name
#         self.age=age
# teacher=School("babu",50)
# pune = School("abu",25)         
# print(teacher.age)
                    #   add methods in class
class Instractor : 
    follower= 2
    def __init__(self,Instractor_name,age):
        self.name=Instractor_name
        self.age=age  
    def display (self,subjet_name)  :
        print(f"hello {self.name}and i teach {subjet_name}")
    def update_follower(self,follower_name):
         self.follower +=2
            
Instractor_1 =Instractor("babu",55)                        
Instractor_2 =Instractor("ameena",25)                        
Instractor_1.display("maths")
Instractor_2.display("python")
Instractor_2.update_follower("anas")
print(Instractor_2.follower)
