s = input().lower()
res = {}
for i in s:
    res[i] = s.count(i)
t = sorted(res, reverse=True)
for key in t[:3]:
    print(key, res[key])