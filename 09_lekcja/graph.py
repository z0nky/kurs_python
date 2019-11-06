# zadanie 1
# Korzystając z dowolnej metody reprezentacji grafu zapisać istniejące połączenia pomiędzy budynkami.

# dom = 0
# szkoła = 1
# kościół = 2
# bar = 3
# szpital = 4
# kino = 5
# tear = 6

graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

places = ['dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr']

# for rows in graph:
#     for obj in rows:
#         if obj == 1:
#
#             print(places[graph.index(rows)], '-', places[rows.index(obj)])
#             #del graph[graph.index(rows)][rows.index(obj)] bez sensu
#         else:
#             continue
#     print()

for row in range(7):
    for col in range(7):
        if graph[row][col] == 1:
            print(places[row], '<--->', places[col])
