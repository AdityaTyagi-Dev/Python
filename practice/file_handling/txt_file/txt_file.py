file = open("sample.txt", "r")

"""
r -> read (default) (used for reading) (gives an error if file doesn't exist)
w -> write (create or rewrites the data if exists)
a -> add (add more text in the end)
r+ -> read and write (gives an error if file doesn't exist)
w+ -> write and read 
"""

content = file.read()
print(content) # print all the content of the sample.txt

print(file.tell()) # tell the cursor's current position
file.seek(0) # move the cursor to the starting position

content2 = file.read(5)
print(content2) # print upto 5 words

file.seek(0) # move the cursor to the starting position

content3 = file.readline()
print(content3) # print only one line from the text file

file.seek(0) # move the cursor to the starting position

content4 = file.readlines()
print(content4) # print all the lines in the form of a list

file.seek(0) # move the cursor to the starting position

content5 = file.readlines(1)
print(content5) # print only 1 line from the beginning

file.close() # close the file

file2 = open("sample2.txt","w")
file2.write("Hello Python\n") # write "Hello Python" in the text file

file2.writelines(["Python is one of the most popular programming language\n", "Python is easy to learn\n"]) # write both the lines in the file

file2.close() # close the file