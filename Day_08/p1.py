with open("data.txt", "r") as f_in:
    lines =[line.strip() for line in f_in.readlines()]

def look(heights, marks, side="l"):  
    for idx, height in enumerate(heights):
        top_idx_l = height.index(max(height))
        top_idx_r = "".join([str(h) for h in height]).rindex(str(max(height)))
        
        if idx==0 or idx == len(heights)-1:
            pass
        elif side=="l":
            marks[idx][top_idx_l] = 1
            for i,h in enumerate(height[:top_idx_l]):
                if [x for x in height[:i] if x >= h]: 
                    marks[idx][i] = 0
        elif side == "r":
            marks[idx][top_idx_r]= 1
            rev_trunc_list = list(reversed(height))[:len(height)-1-top_idx_r]
            rev_trunc_enum = list(reversed(list(enumerate(height))))[:len(height)-1-top_idx_r]
            c = 0 
            for i,h in rev_trunc_enum:
                if [x for x in rev_trunc_list[:c] if x >= h]: 
                    marks[idx][i] = 0
                c+=1
            hidden_no = len(height[top_idx_l+1:top_idx_r])
            if hidden_no > 0: marks[idx][top_idx_l+1:top_idx_r] = hidden_no*[0]
                
    return marks

def count_trees(mark_map):
    counter = 0
    for line in mark_map:
        counter+=sum([1 for x in line if x > 0])
    return counter

def transpose_list(to_transpose):
    return list(map(list, zip(*to_transpose)))

heights = []  # height of trees 
marks_LR = [] # mask of map with 0: unseen, 1: seen
marks_UD = [] # for looking LeftRight and UpDown
for line in lines:
    heights.append([int(i) for i in line])
    marks_LR.append(len([i for i in line])*[1])
    marks_UD.append(len([i for i in line])*[1])

marks_UD = transpose_list(marks_UD)

marks_LR = look(heights, marks_LR, "l")
marks_LR = look(heights, marks_LR, "r")

heightsT = transpose_list(heights)

marks_UD = look(heightsT, marks_UD, "l")
marks_UD = look(heightsT, marks_UD, "r")

marks_UD = [list(i) for i in zip(*marks_UD)]
combined_map = [[x + y for x, y in zip(mark, marks_UD[idx])] for idx, mark in enumerate(marks_LR)]

print(count_trees(combined_map))  
