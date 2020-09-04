# File IO Basics
"""
"r" - Open file for reading --> Default
"w" - Open a file for writing
"x" - Creates a file if not exists
"a" - Add more content to a file
"t" - text mode --> Default
"b" - Binary mode 
"+" - Read and Write
"""

f = open("harsh.txt", "rt") #Can leave 2nd argument Empty and will mean same
print(f.readlines()) #This converts file into a list

# print(f.readline())
# print(f.readline())

# cont = f.read()

# for line in f:
#     print(line, end="")
    
# print(content)

# content = f.read(34442)
# print("1", content)

# content = f.read(322222)
# print("2", content)

f.close()
