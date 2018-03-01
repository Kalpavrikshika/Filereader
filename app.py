from read_line_py3 import Filereader
freader_object = Filereader()

input_file = "stuff.txt"

current_file = open(input_file,"r")

print("Printing all")
r = freader_object.read_all(current_file)
print r
print("\n\n")


print ("rewind the file")
s = freader_object.rewind(current_file, 0)
print s
print("\n\n")

print ("printing 2 lines")
current_line = 1
line_1 = freader_object.get_line(current_file)
print line_1
print("\n\n")

current_line = current_line + 1
line_2 = freader_object.get_line(current_file)
print line_2