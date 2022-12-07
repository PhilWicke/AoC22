with open("data.txt", "r") as f_in:
    lines =[line.strip() for line in f_in.readlines()]

def get_size(dir_name, ls_list, dir_size=0):
    for item in ls_list:
        if item.split(" ")[0].isdigit():
            dir_size += int(item.split(" ")[0])
            if dir_size > 100000:
                break
        else:
            sub_dir = dir_name+"/"+item.split(" ")[1]
            is_small, sub_size = get_size(sub_dir, main[sub_dir])
            dir_size+=sub_size
            if is_small and dir_size <= 100000:
                pass
            else:
                return 0, dir_size
    if dir_size > 100000:
        return 0, dir_size
    else:
        tested.append((dir_name, dir_size))
        return 1, dir_size
        
main = dict()
pwd = "."
for i in range(0,len(lines)):
    if lines[i]=="$ ls":
        pass
    elif lines[i]=="$ cd ..":
        pwd = pwd[:pwd.rfind("/")]
    elif lines[i].startswith("$ cd "):
        dir_name = lines[i].split(" ")[2]
        if dir_name != "/":
            pwd += "/"+dir_name
        if pwd not in main.keys():
            main[pwd] = []
    else:
        main[pwd].append(lines[i])

tested = []
[get_size(dir_name, ls_list) for dir_name, ls_list in main.items()]
file_sum = 0
for a,b in list(set(tested)):
    file_sum+=b
print(file_sum)
