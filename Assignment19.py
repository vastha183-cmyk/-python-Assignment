#name-Astha vishwakarma
#Roll number-23
#Assignment-19
list=[1,1,0.1,0,1,1]
present=0
absent=0
for a in list:
    if a ==1:
        present+=1
    else:
        absent+=1
total=len(list)
percentage=(present/total)*100
print("present:",present)
print("absent:",absent)
print("list :",percentage)