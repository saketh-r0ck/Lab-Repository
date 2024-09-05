class Bipartite_Matching:
    def __init__(self, graph):
        self.graph = graph
        self.workers = len(graph[0])
        self.tasks = len(graph)

    def bipartite_match(self,u, visited, assign):
        for v in range(self.workers):
            if graph[u][v] and not visited[v]:
                visited[v] = True
                if assign[v] == -1 or self.bipartite_match(assign[v], visited, assign):
                    assign[v] = u
                    return True
        return False

    def max_match(self):
        assign = [-1] * self.workers
        
        for u in range(self.tasks):
            visited = [False] * self.workers
            self.bipartite_match(u, visited, assign)

        for w in range(self.workers):
            if assign[w] != -1:
                
                print(f" Task ID {assign[w]+1} -> Worker ID {w+1} ")

    

if __name__ == "__main__":
    t , w = map(int,input("first line : ").split())
    graph = []
    for i in range(t):
        qualified_workers = [0]*w
        tup = input().split(",")[1:]
        for j in tup:
            qualified_workers[int(j)-1] = 1
        graph.append(qualified_workers)

    match = Bipartite_Matching(graph)
    print("Output Matchings : ")
    match.max_match()
    


