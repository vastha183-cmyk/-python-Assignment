#name-Astha vishwakarma
#Roll number-23
#Assignment-22
#Question-A cricket player scored runs in 6 matches.
#example:[45,60,10,80,55,90]
#write a program to:
#find total runs
#find highest score
#count how many matches player scored more than 50 runs
runs=[45,60,10,80,55,90]
total_runs=sum(runs)
highest_score=max(runs)
count_50_plus=0
for r in runs:
    if r > 50:
        count_50_plus+=1
print("Total runs:",total_runs)
print("highest score:",highest_score)
print("matches with more than 50 runs:",count_50_plus)