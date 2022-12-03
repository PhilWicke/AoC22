with open("data.txt", "r") as f_in:
    lines = f_in.readlines()

count = 0
for line in lines:
    midpoint = int(len(line)/2)
    x = str(set([i for i in line[:midpoint] if i in line[midpoint:]]))[2]
    if x.isupper():
        count += ord(x) - 38
    if x.islower():
        count += ord(x) - 96
print(count)
