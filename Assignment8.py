#name-Astha vishwakarma
#Roll number-23
#Assignment-8
#Question-given a list of numbers 1-20,create a new list that contains only the even numbers.
nums=list(range(1,21))
even=[]
for i in nums:
    if i % 2==0:
        even.append(i)
print(even)