with open("data.txt", "r") as f_in:
    lines = f_in.readlines()

mat_pt = {"X":1,"Y":2,"Z":3}
res = 0
for line in lines:
    opp, me = line.split(" ")
    me = me.strip()
    if me == "X": # loss
        if opp=="A":
            res += 3
        elif opp=="B":
            res += 1
        elif opp=="C":
            res += 2
    elif me == "Y": # draw
        if opp=="A":
            res += 1+3
        elif opp=="B":
            res += 2+3
        elif opp=="C":
            res += 3+3
    elif me == "Z": # win
        if opp=="A":
            res += 2+6
        elif opp=="B":
            res += 3+6
        elif opp=="C":
            res += 1+6    
print(res)

