file = open("textfile.txt")
contents = file.read()
print(contents)

file.close()


with open("new_file.txt", mode="w") as file:
    file.write("\nCreating new file")


with open("/Users/TechPro/Desktop/New_file.txt") as new_file:
    contents = new_file.read()
    print(contents)