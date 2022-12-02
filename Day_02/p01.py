with open("data.txt", "r") as f_in:
    lines = f_in.readlines()

mat_pt = {"X":1,"Y":2,"Z":3}
res = 0
for line in lines:
    opp, me = line.split(" ")
    me = me.strip()
    if (opp=="A" and me=="X") or (opp=="B" and me=="Y") or (opp=="C" and me=="Z"):
        res += 3 + mat_pt[me]
    elif (opp=="A" and me=="Z") or (opp=="B" and me=="X") or (opp=="C" and me=="Y"):
        res += mat_pt[me]
    elif (opp=="A" and me=="Y") or (opp=="B" and me=="Z") or (opp=="C" and me=="X"):
        res += 6 + mat_pt[me]
print(res)




