with open("data.txt", "r") as f_in:
    lines =[line.strip() for line in f_in.readlines()]#[:55]

def get_size(dir_name, ls_list, dir_size=0):
    for item in ls_list:
        if item.split(" ")[0].isdigit():
            dir_size += int(item.split(" ")[0])
        else:
            sub_dir = dir_name+"/"+item.split(" ")[1]
            sub_size = get_size(sub_dir, main[sub_dir])
            dir_size+=sub_size
    sizes.append((dir_name, dir_size))
    return dir_size

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

sizes = []
total_size = get_size(".", main["."])
unused_space = 70000000 - total_size
needed_space = 30000000 - unused_space

print(min([size[1] for size in sizes if size[1]-needed_space>=0]))
 
