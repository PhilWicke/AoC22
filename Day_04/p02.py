with open("data.txt", "r") as f_in:
    lines = f_in.readlines()
    lines = [line.strip() for line in lines]

count = 0
for line in lines:
    a, b = line.split(",")
    a, b = a.split("-"), b.split("-")
    if int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1]):
        count+=1
    elif int(b[0]) >= int(a[0]) and int(b[0]) <= int(a[1]):
        count+=1

print(count)
