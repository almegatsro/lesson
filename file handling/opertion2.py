file_read = open("Codingal.txt", "r")
print("file is in read mode")
print(file_read.read())
file_read.close()   

file_write = open("Codingal.txt", "w")
print("file is in write mode")
file_write.write("This is a new line added to the file.\n")
file_write.close()

file_append = open("Codingal.txt", "a")

print("file is in append mode")
file_append.write("This line is appended to the file.\n")
file_append.close()
