#name-Astha vishwakarma
#Roll number-23
#Assignment-7
#Question-ask a user for a fruit name.check if it exists in your fruit_basket list using the in keyword.
fruit_basket=["apple","banana","mango","orange"]
fruit=input("Enter fruit name:")
if fruit in fruit_basket:
    print("fruit_exists")
else:
    print("fruit not found")