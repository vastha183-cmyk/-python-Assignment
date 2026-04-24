#Name-Astha vishwakarma
#Roll no-23
#Practical no-46
#Question-
menu={"samosa":10,"chaumeen":5,"nudalsh":20}
cart=[]
while True:
    item=input("Enter item:")
    if item=="done":
        break
    if item in menu:
        cart.append(item)
    else:
        print("not available")
total=0
for i in cart:
    total+=menu[i]
print("items:",cart)
print("total:",total)