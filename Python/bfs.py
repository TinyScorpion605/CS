graph = {"A":["B", "C"], "B":["D", "E"], "C":["F"], "D":[], "E":[], "F":["G"], "G":[]}
start = "A"
target = "D"
target_found = False

visited = []
path = []
wait = []

visited.append(start)
path.append(start)
wait.append(start)
node = visited[0]

while wait != []:
    if wait[0] not in visited:
        visited.append(wait[0])
        path.append(wait[0])    
        wait.remove(wait[0])

    elif wait[0] in visited:
        wait.remove(wait[0])

    for neighbor in graph[node]:
        if graph[neighbor] == [] and graph[neighbor] != target:
            wait.append(neighbor)
            if neighbor in path:
                path.remove(neighbor)
            
            neighbor = wait[-2]
            node = visited[-2]
        else:
            node = neighbor
            wait.append(node)
            
print(wait)
print(visited)
print(path)