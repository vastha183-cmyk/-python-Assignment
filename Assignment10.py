#name-Astha vishwakarma
#Roll number-23
#Assignment-10
#Question-given a list of 10 students marks,count how many students scored above 40.
marks=[35,50,42,60,30,80]
count=0
for m in marks:
    if m > 40:
        count+=1
print("students scored above 40:",count)