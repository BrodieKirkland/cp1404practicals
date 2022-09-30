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

total = 0
in_file = open("numbers.txt", "r")
for i in range(2):
    line = in_file.readline()
    total += int(line)
in_file.close()
print(f"Total from numbers.txt: {total}")
