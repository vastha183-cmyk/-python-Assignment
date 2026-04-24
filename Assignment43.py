#Name-Astha vishwakarma
#Roll no-23
#Practical no-46
#Question-
att={"A":1,"B":0,"C":1,"D":0,"E":1}
present=sum(att.values())
print("present:",present)
print("absent students:")
for s,v in att.items():
    if v == 0:
        print(s)