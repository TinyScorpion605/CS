# Breadth First Search Algorithm

graph = {   
    "A": ["B", "C", "D", "E"],
    "B": ["E", "F", "G"],
    "C": ["F", "G", "H", "I"],
    "D": ["H", "I", "J", "K"],
    "E": ["J", "K", "L", "A"], 
    "F": ["K", "L", "M"],    
    "G": ["L", "M", "N", "O"],
    "H": ["M", "N", "O", "P"],
    "I": ["N", "O", "P"],
    "J": ["P", "Q", "R", "S"],
    "K": ["Q", "R", "S", "T"], 
    "L": ["R", "S", "U"],
    "M": [],         
    "N": ["U", "V", "W"],
    "O": ["U", "V", "X"],
    "P": ["V", "W", "Y"],
    "Q": ["W", "X"],
    "R": ["X", "Y", "A"],   
    "S": ["Y", "B", "C"],
    "T": [],           
    "U": ["F", "G"],
    "V": ["T"],          
    "W": ["C", "J"],
    "X": ["M"],              
    "Y": ["E", "N"],
    "Z": []               
}

start = "A"
target = "O"
target_found = False
traversed = []
queue = [[start]]
visited = [start]

while queue:
    path = queue.pop(0)
    node = path[-1]

    traversed.append(node)
    print(node)

    if node == target:
        print("Path Found:", path)
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(path + [neighbor])
else:
    print("Target not found.")