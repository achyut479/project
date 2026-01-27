# program to count number of lines in the file
# opening a file
file = open('achyut.txt')
counter = 0

# reading from file
content = file.read()
# splitting content into lines
# and storing them in the list 
colist = content.split("\n")

for i in colist:
  
