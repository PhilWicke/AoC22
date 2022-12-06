with open("data.txt", "r") as f_in:
    line = f_in.readline().strip()
for i in range(0,len(line)):
    if len(set(line[i:i+4])) == 4:
        print(i+4)
        break
 

        

    
