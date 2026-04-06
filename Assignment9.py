#name-Astha vishwakarma
#Roll number-23
#Assignment-9
#Question-write a program thattakes a list of names and a "search_name" form the user. print the user.print the index where the name is found,or "not found".
names=["aman","riya","sita","rohit"]
search=input("Enter name:")
if search in names:
    print("index:",names.index(search))
else:
    print("name not found")