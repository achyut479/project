# parent class
class person( object ):

       #_init_is known as the constructor
       def _init_(self, name, idnumber):
               self.name = name
               self.idnumber = idnumber
       def display(self):
               print("name:",self.name)
              print("id number:",self.idnumber)

# child class
class employee( person ):
        def _init_(self, name, idnumber, salary, post):
               self.salary = salary
               self.post = post

                # invoking the _init_of the parent class
                person._init_(self, name, idnumber,)

# creation of an object variable or an instance
a = employee('penguin', 20192010, 10203, "MP")

# calling the function person using instance
a.display()
  
              
