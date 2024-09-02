def merge_queries(dbs,queries):
  
  for query in queries:
    if query[0] != query[1]:
        dbs[query[1]-1] += dbs[query[0]-1]  
    print(max(dbs))

def main(): 

    first_line = input("first line : ").split()
    n , m = map(int,first_line)
    second_line = input('Second line: ').split()
    dbs = list(map(int,second_line))
    
    query_lines = []
    print("Input Queries : ")
    for i in range(m):
        src , dest = map(int,input().split())
        query_lines.append((src,dest))
    print("Output : ")
    merge_queries(dbs,query_lines)

if __name__ == "__main__":
    main()