with open("data.txt", "r") as f_in:
    lines = f_in.readlines()

count = 0
for i in range(0,len(lines),3):
    x = [w for w in lines[i+2] if w in [v for v in lines[i] if v in lines[i+1]]][0]
    if x.isupper(): count += ord(x) - 38
    if x.islower(): count += ord(x) - 96
print(count)
