with open("data.txt", "r") as f_in:
    lines = f_in.readlines()

count = 0
for line in lines:
    x = [i for i in line[:int(len(line)/2)] if i in line[int(len(line)/2):]][0]
    if x.isupper(): count += ord(x) - 38
    if x.islower(): count += ord(x) - 96
print(count)
