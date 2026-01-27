# open the file in read mode
file_read = open('achyut.txt')
print("file in read mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('achyut.txt')
# write in the file
file_write.write("file in the write mode ....")
file_write.write("hi! i am achyut , i am 16 years old")
file_write.colse()

# open the file in append mode
file_append = open('achyut.txt')
file_append.write("\n file in append mode")
file_append.write("hi! i am achyut")
file_append.close()
