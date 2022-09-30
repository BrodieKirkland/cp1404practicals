# 1.

name = input("Name: ")
file_name = f"{name}.txt"
out_file = open(file_name, "w")
print(name, file=out_file)
out_file.close()

# 2.

in_file = open(file_name, "r")
print(f"Your name is {in_file.read()}")
in_file.close()

# 3.

