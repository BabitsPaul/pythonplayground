from util.lp import fact

ls = [1]
for i in range(2, 10):
    ls.append(ls[i - 2] * i)

print(ls)

for i in range(3, 3625920):
    if i == sum([fact(int(j)) for j in str(i)]):
        print(i)
