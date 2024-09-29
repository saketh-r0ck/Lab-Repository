def minimizeCost(k, arr):
        
    current_step = 0
    total_cost = 0
 
    
    while current_step!=len(arr)-1:
        next_step = 0
        mincost = float('inf')
        for j in range(1,k+1):
           

            if current_step+j<len(arr) and mincost >= abs(arr[current_step]-arr[current_step+j]):
                
                mincost = abs(arr[current_step]-arr[current_step+j])
                next_step = current_step+j       
                #print(next_step)

        current_step = next_step
        total_cost += mincost 
        print(total_cost)
    

if __name__ == "__main__":
    minimizeCost(3,[10,30,40,50,20])