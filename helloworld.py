
def find_p(jobs,end_idx):
		
	low = 0
	high = end_idx
	while low <= high:
		mid = (low + high) // 2
		
		if jobs[mid][1] <= jobs[end_idx][0]:
			if jobs[mid+1][1] <= jobs[end_idx][0]:
				low = mid + 1
			else: 
				return mid + 1
		else:
			high = mid - 1 
	return 0



	
def find_max_weight(jobs):

	jobs.sort(key=lambda x:x[1])
	print(jobs)
	
	p = [0]*len(jobs)
	for i in range(len(jobs)):
		p[i] = find_p(jobs,i)
	#print(p)
	
	opt = [0]*(len(jobs)+1)
	for j in range(1,len(jobs)+1):
		opt[j] = max(jobs[j-1][2] + opt[p[j-1]] , opt[j-1])

	
	selected_intervals = []
	j = len(jobs)
	while j > 0:
		if jobs[j - 1][2] + opt[p[j - 1]] > opt[j - 1]:  
			selected_intervals.append(j - 1) 
			j = p[j - 1]  
		else:
			j -= 1 
	
	return opt , selected_intervals


if __name__ == '__main__':

    genes = [(10,100,0.234)]
    optimal , included = find_max_weight(genes)
    for i in range(len(included)-1,-1,-1):
        print("Included : " + str(genes[included[i]]))
    print("Sum Probability : " + str(optimal[-1]))
    
    genes2 = [(10, 100, 0.234), (50, 150, 0.456), (120, 200, 0.678), (180, 250, 0.789), (210, 300, 0.321)]
    opt , included = find_max_wight