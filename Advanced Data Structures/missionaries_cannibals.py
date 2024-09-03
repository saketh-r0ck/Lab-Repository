
def is_valid(state):
    m1 , c1 ,b ,m2 ,c2 = state
    return 0<=m1<=3 and 0<=c1<=3 and 0<=c2<=3 and 0<=m2<=3 and ((m1==0 or m1>=c1) and (m2==0 or m2>=c2))

def generate_next_states(state):
    m1 , c1 ,b ,m2 ,c2 = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    next_states = []
    for dm ,dc in moves:
        if b == 1:  
            new_state = (m1-dm, c1-dc , 0 , m2+dm, c2+dc)
        else:
            new_state = (m1+dm , c1+dc , 1 , m2-dm , c2-dc)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

def solve_bfs(state_state):
    queue = [(start_state, [start_state])]
    while queue:
        current_state , path = queue.pop(0)
        if current_state == (0,0,0,3,3):
            return path
        for next_state in generate_next_states(current_state):
            if next_state not in path:
                queue.append((next_state , path +[next_state]))
    return None

if __name__ == "__main__":
    start_state = (3,3,1,0,0)
    solution_paths = solve_bfs(start_state)
    # if solution_paths:
    #     for state in solution_paths:
    #         m1 , c1 , b, m2 , c2 = state
    #         print(f"{m1} missionaries ,{c1} cannibals, {'boat on left' if b==1 else 'boat on right'}, {m2} missionareis , {c2} cannibals")
    # else:
    #     print("No solution")
    if solution_paths:
        for i in range(1, len(solution_paths)):
            m1_prev, c1_prev, b_prev, m2_prev, c2_prev = solution_paths[i - 1]
            m1, c1, b, m2, c2 = solution_paths[i]

            if b == 0:
                print(f"Crossing: {m1_prev - m1} M and {c1_prev - c1} C cross from left to right")
            else:
                print(f"Crossing: {m2_prev - m2} M and {c2_prev - c2} C cross from right to left")

        # Final state
        m1, c1, b, m2, c2 = solution_paths[-1]
        print(f"Final State: {m1} M, {c1} C on the left; {m2} M, {c2} C on the right")
    else:
        print("No solution")