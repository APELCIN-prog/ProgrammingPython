N = int(input())
res = [True] * (N + 1)
res[0] = res [1] = False
for i in range(2, int(N ** 0.5) + 1):
    if res[i]:
        for g in range(i**2, N + 1, i):
            res[g] = False


for num in range(2, N+1):
    if res[num]:
        print(num)