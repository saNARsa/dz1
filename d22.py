import random
password = []
x = random.randint(3, 20)
for i in range(20):
    for j in range(1 , i):
        if i == 0 or j == 0:
            continue
        if x % (i + j) == 0:

            password.append((j,i))

print(x)
print(password)