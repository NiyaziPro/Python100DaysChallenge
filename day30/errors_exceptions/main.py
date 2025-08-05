# FileNotFound
# with open("a_file.txt") as file:
#   file.read()

# KeyError
# dictionary = {"key": "value"}
# value = dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple","Mango", "Lemon"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
 file = open("a_file.txt")
 dictionary = {"key": "value"}
 print(dictionary["key"])
except FileNotFoundError:
 file = open("a_file.txt","w")
 file.write("Something...")
except KeyError as error_message:
 print(f"The key {error_message} does not exist.")
else:
 content = file.read()
 print(content)
finally:
 file.close()
 print("File was closed.")

