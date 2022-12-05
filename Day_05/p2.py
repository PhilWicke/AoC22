#[F]         [L]     [M]            
#[T]     [H] [V] [G] [V]            
#[N]     [T] [D] [R] [N]     [D]    
#[Z]     [B] [C] [P] [B] [R] [Z]    
#[M]     [J] [N] [M] [F] [M] [V] [H]
#[G] [J] [L] [J] [S] [C] [G] [M] [F]
#[H] [W] [V] [P] [W] [H] [H] [N] [N]
#[J] [V] [G] [B] [F] [G] [D] [H] [G]
# 1   2   3   4   5   6   7   8   9 

with open("data.txt", "r") as f_in:
    lines = f_in.readlines()
    lines = [line.strip() for line in lines]


stacks = {somelist: [] for somelist in range(1,10) }
moves = []
for line in lines:
    if line.startswith("move"):
        c = line.split(" ")
        moves.append((c[1], c[3], c[5]))
    else:
        for j,i in enumerate(range(0, len(line), 4)):
            stacks[j+1].append(line[i+1:i+2])
            
for i, stack in stacks.items():
    del stack[-1]
    stacks[i] = [s for s in stack if s!=" "]

for move in moves:
    pack_num, src, trg = int(move[0]), int(move[1]), int(move[2]) 
    select = stacks[src][:pack_num]
    del stacks[src][:pack_num]
    #select.reverse()
    stacks[trg][:0] = select


res = ""
for i in stacks.values():
    res+=i[0]
print(res)
