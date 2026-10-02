N = int(input())
numbers = [10**i * 9 * len(str(10**i)) for i in range(15)]
count = 0
flag = False
for n in numbers:
    count += 1
    if n >= N:
        if flag:
            break
        size = sum(numbers[:count-1])
        poradoc_in_group = N - size
        step = count
        for i in range(10**(len(str(N))-1), 10**len(str(N))):
            if flag:
                break
            poradoc_in_group -= step
            if poradoc_in_group <= 0:
                poradoc_in_group += step
                for j in str(i):
                    poradoc_in_group -= 1
                    if poradoc_in_group == 0:
                        print(j)
                        break
                flag = True
                break
