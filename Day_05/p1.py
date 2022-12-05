with open("data.txt", "r") as f_in:
    lines = f_in.readlines()
    lines = [line.strip() for line in lines]

stacks = {somelist: [] for somelist in range(1,10) }
moves = []
for line in lines:
    if line.startswith("move"): # parse moves
        c = line.split(" ")
        moves.append((c[1], c[3], c[5]))
    else:                       # parse stacks
        for j,i in enumerate(range(0, len(line), 4)):
            stacks[j+1].append(line[i+1:i+2])
            
for i, stack in stacks.items(): 
    del stack[-1] # rmv stack label 
    stacks[i] = [s for s in stack if s!=" "] # rmv empty crates

for move in moves:
    pack_num, src, trg = int(move[0]), int(move[1]), int(move[2]) 
    select = stacks[src][:pack_num] # select crates
    del stacks[src][:pack_num] # remove selected
    select.reverse() # turn order (!)
    stacks[trg][:0] = select # insert selected

res = "" # print result
for i in stacks.values():
    res+=i[0]
print(res)
