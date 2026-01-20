class person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class student(person):
  def _init_(self, fname, lname, year):
    super()._init_(fname, lname)
    self.graduationyear = year

x = student("joey", "king", 2021)
x.printname()
print(x.graduationyear)
