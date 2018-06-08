from sys import argv
script, filename = argv
print(f"Here's your file {filename}:")
txt = open(filename)
print(txt.read())
print("Type the filename again:")  
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
