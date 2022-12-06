with open("data.txt", "r") as f_in:
    line = f_in.readline().strip()
for i in range(0,len(line)):
    if len(set(line[i:i+14])) == 14:
        print(i+14)
        break
 

        

    
