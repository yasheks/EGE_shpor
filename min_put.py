n, start, f = map(int, input().split())
start -= 1
f -= 1
w = [list(map(int, input().split())) for i in range(n)]
# Избавимся от -1; матрица смежности графа,
# где -1 означает отсутствие ребра между вершинами
INF = 10 ** 10
for i in range(n):
    for j in range(n):
        if w[i][j] == -1:
            w[i][j] = INF
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start

while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if dist[i] + w[i][j] < dist[j]:
            dist[j] = dist[i] + w[i][j]
    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
if dist[f] != 10 ** 10:
    print(dist[f])
else:
    print(-1)
