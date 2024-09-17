
def find_p(jobs,finish):
	large_index = 0
	end = jobs[finish]
	for i in jobs:
		print(large_index)
		if i == end:
			return large_index
		if i[1] <= end[0]:
			large_index = max(large_index,i[0])
		


def find_max_wight(jobs):
	print(jobs)
	jobs.sort(key=lambda x:x[1])
	print(jobs)
	
	p = [0]*len(jobs)
	#for i in range(len(jobs)):
	p[3] = find_p(jobs,3)
	print(p)



if __name__ == '__main__':
    jobs = [(0,3,3),(1,4,2),(3,6,1),(0,5,4),(4,7,2),(3,9,5),(5,10,2),(8,10,1)]
    find_max_wight(jobs)