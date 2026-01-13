class parrot:

  # instance attributes
  def_init_(self,name,age):
     self.name = name
     self.age = age

# instance method
def sing(self, song):
    return "{} sings {}".formet(self.name, song)

def dance(self):
  return "{} is now dancing {}".formet(self.name)

# institiate the object
blu = parrot("blu", 10)

# call our instance methods
print(blu.sing('"happy"'))
print(blu.dance())
