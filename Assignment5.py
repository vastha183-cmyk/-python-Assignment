#name-Astha vishwakarma
#Roll number-23
#Assignment-5
#Question-create a list of 10 random integers.use a for loop to print each number multiplied by 2.
import random
numbers=[random.randint(1,100)for i in range(10)]
for n in numbers:
    print(n*2)