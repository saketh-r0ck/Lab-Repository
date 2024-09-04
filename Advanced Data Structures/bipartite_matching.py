graph = [[1,1,0,0,1,1],
         [1,0,1,0,0,0],
         [0,0,1,1,0,0],
         [0,0,0,1,0,1],
         [0,1,0,1,1,0]]

workers = len(graph[0])
tasks = len(graph)

def bipartite_match(u, visited, assign):
    for v in range(workers):
        if graph[u][v] and not visited[v]:
            visited[v] = True
            if assign[v] == -1 or bipartite_match(assign[v], visited, assign):
                assign[v] = u
                return True
    return False

def max_match():
    assign = [-1] * workers
    
    for u in range(tasks):
        visited = [False] * workers
        bipartite_match(u, visited, assign)

    # Create the match output in "t1 -> w1" format
    for w in range(workers):
        if assign[w] != -1:
            
            print(f" t{assign[w]+1} -> w{w+1} ")

    

if __name__ == "__main__":
    max_match()
    


