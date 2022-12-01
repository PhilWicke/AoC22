with open("data.txt", "r") as dat_in:
    lines = dat_in.readlines()

vals = []
t_sum = 0
for line in lines:
    line = line.strip()
    if line.isdigit():
        t_sum+=int(line)
    else:
        vals.append(t_sum)
        t_sum=0

print(sum(sorted(vals, reverse=True)[:3]))
