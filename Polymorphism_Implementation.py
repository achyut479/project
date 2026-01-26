class cat:
  def _init_(self, name, age):
      self.name = name
      self.age = age

  def info(self):
      print(f"I am a cat. my name is{self.name}. I am {self.age}years old.")

  def make_sound(self):
      print("meow")


class dog:
  def _init_(self, name, age):
      self.name = name
      self.age = age

  def info(self):
      print(f"I am a dog. my name is{self.name}. I am {self.age}years old.")

  def make_sound(self):
      print("bark")

cat1 = cat("dado", 2.5)
dog1 = dog("tyson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
      
