file = open("textfile.txt")
contents = file.read()
print(contents)

file.close()


with open("new_file.txt", mode="w") as file:
    file.write("\nCreating new file")
