# WAP to count number of words and lines in a file

file_name = input("Enter file name: ")

with open(file_name, "r") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

print("Number of lines:", line_count)
print("Number of words:", word_count)
