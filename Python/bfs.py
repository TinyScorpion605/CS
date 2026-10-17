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
target = "M"
target_found = False

visited = []
path = []
wait = []

visited.append(start)
path.append(start)
wait.append(start)

queue = [[start]]

while wait and not target_found:
    current_path = queue.pop(0)
    wait.pop(0)
    node = current_path[-1]
    
    if node == target:
        target_found = True
        path = current_path
        break
        
    if node not in visited:
        visited.append(node)
        
    for neighbor in graph[node]:
        if neighbor not in visited and neighbor not in [p[-1] for p in queue]:
            new_path = list(current_path)
            new_path.append(neighbor)
            queue.append(new_path)
            wait.append(neighbor)

if target_found:
    print("Path Found: ", path)
else:
    print("Target not found.")