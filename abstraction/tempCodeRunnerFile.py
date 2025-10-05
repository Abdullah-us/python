from abc import ABC, abstractmethod

class person(ABC):
   
   @abstractmethod
   def show(self):
      pass
   
class student(person):
    def __init__(self,name,age):
          self.name=name
          self.age=age

    def show(self):
              print(f"Student name is{self.name} and student age is {self.age}")

s = [
     student("Abdullah",22),
     student("Asif",21),
     student("Ali",20),
     student("Abdullah khan",23)
]

for i in s:
    i.show()


          