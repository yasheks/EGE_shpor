def F(t1, t2):
    return ((t2[0] - t1[0]) ** 2 + (t2[1]-t1[1]) **2) ** 0.5 #функция поиска центроида
f = open("27_A_17916.txt")
f.readline()
c = [[], []]#количество кластеров
k = 0
for s in f:
    x, y = map(float, s.replace(",", ".").split())
    k += 1
    if y > 8:#условие для разделения
        c[0].append((x, y))
    else:
        c[1].append((x, y))
print(len(c[0]), len(c[1]), k)

mn = [10**10]*len(c) #хз че эта
T = [0] * len(c)
for i in range(len(c)):
    for t1 in c[i]:
        s= 0
        for t2 in c[i]:
            s += F(t1, t2)
        if s < mn[i]:
            mn[i] = s
            T[i] = t1
px = int(sum([x for x,y in T])/len(c)*10000)
py = int(sum([y for x,y in T])/len(c)*10000)
print(px, py)

