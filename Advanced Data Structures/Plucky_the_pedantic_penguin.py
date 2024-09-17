
def greedy_algorithm(holes,m,t):
    
    current_pos = 0
    output = []
    i = 0
    output.append(holes[0])
    while current_pos < t:
        last_pos = current_pos
        while i < len(holes) and holes[i]-current_pos <=m:
            last_pos = holes[i]
            i += 1 
        
        if last_pos == current_pos:
            return "Stay Home"
        if last_pos !=t :
            output.append(last_pos)
        current_pos = last_pos
    output.append(t)
    print(output)
        

if __name__ == "__main__":
    
    holes = list(map(int,input("List of holes : ").split()))
    m = int(input("m : "))
    t = holes[-1]
    greedy_algorithm(holes,m,t)