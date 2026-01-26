class computer:

   def _init_(self):
       self._maxprice = 900

   def sell(self):
       print("selling price: {}".format(self._maxprice))

   def setmaxprice(self, price):
      self._maxprice = price
     
c = computer()
c.sell()

#change the price
c._maxprice = 1000
c.sell()

# using setter function
c.setmaxprice(1000)
c.sell()
