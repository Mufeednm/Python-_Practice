# class dog:
#     def walk (self):
#         print("i can walk")
#     def swim (self):
#         print ("i can swim")
# class  cat :
#     def walk(self):
#         print("i can walk")          
#     def swim (self):
#         print("i can swim")
# class baby :
#     pass           
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_quack(obj):
    obj.quack()

# Both Duck and Person classes have a 'quack' method.
# Even though they are different types, as long as they have the 'quack' method,
# they can be used interchangeably.
duck = Duck()
person = Person()

make_quack(duck)    # Output: Quack!
make_quack(person)  # Output: I'm quacking like a duck!
