#name-Astha vishwakarma
#Roll number-23
#Assignment-22
marks=[78,35,90,40,55]
pass_student=[]
for i in marks:
    if(i>40):
        pass_student.append(i)
        print("pass")
    else:
        print("Fail")
print("all marks:",marks)
total=sum(marks)
avg=total/len(marks)
print("total",total)
print("avg",avg)