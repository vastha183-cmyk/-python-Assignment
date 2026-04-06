#name-Astha vishwakarma
#Roll number-23
#Assignment-11
#Question-take a list like [-5,3,-2,8].create a new list where all negative numbers are converted to positive.
lst=[-5,3,-2,8]
new_list=[]
for i in lst:
    if i < 0:
        new_list.append(-i)
    else:
        new_list.append(i)
print(new_list)