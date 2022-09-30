# # 1.
#
name = input("Name: ")
file_name = f"{name}.txt"
out_file = open(file_name, "w")
print(name, file=out_file)
out_file.close()

# # 2.
#
in_file = open(file_name, "r")
print(f"Your name is {in_file.read()}")
in_file.close()
#
# # 3.
#
total = 0
in_file = open("numbers.txt", "r")
for i in range(2):
    total += int(in_file.readline())
in_file.close()
print(f"Total from numbers.txt: {total}")

# 4.

total = 0
file_name = input("File name: ")
in_file = open(file_name, "r")
for line in in_file:
    total += int(line)
in_file.close()
print(f"Total from {file_name}: {total}")