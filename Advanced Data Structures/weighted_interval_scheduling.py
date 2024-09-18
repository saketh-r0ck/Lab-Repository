
def find_p(jobs,end_idx):
	end = jobs[end_idx]
	#cnt = 0		
	#for i in jobs:
	#	
	#	if i == end:
	#		return cnt
	#	if i[1] <= end[0]:
	#		cnt +=1
			
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



	
def find_max_wight(jobs):

	jobs.sort(key=lambda x:x[1])
	print(jobs)
	
	p = [0]*len(jobs)
	for i in range(len(jobs)):
		p[i] = find_p(jobs,i)
	print(p)
	
	opt = [0]*(len(jobs)+1)
	for j in range(1,len(jobs)+1):
		opt[j] = max(jobs[j-1][2] + opt[p[j-1]] , opt[j-1])
	
	return opt


if __name__ == '__main__':
    jobs = [(0,3,3),(1,4,2),(3,6,1),(0,5,4),(4,7,2),(3,9,5),(5,10,2),(8,10,1)]
    optimal = find_max_wight(jobs)
    print(optimal)
