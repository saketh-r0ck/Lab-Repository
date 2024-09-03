class Gale_Shapely:
	def __init__(self,proposing,proposed):
		self.men_match = [None]*len(proposing)
		self.woman_match = [None]*len(proposed)
		self.free_man = list(proposing.keys())
		self.man = proposing
		self.woman = proposed
		
		
	
	def stable_matching(self,men_preference,women_preference):
		while len(self.free_man) >0:
			m = self.free_man.pop(0)
			
			m_list = men_preference[self.man[m]]
			for w in m_list:
				women_idx = self.woman[w]

				engaged = self.woman_match[women_idx]
				print(str(m) + " "+ str(engaged))
				if engaged is None:
					self.men_match[self.man[m]] = w
					
					self.woman_match[self.woman[w]] = m
					
					break
				else: 
					w_list = women_preference[women_idx]
					if w_list.index(m) < w_list.index(engaged):
						self.men_match[self.man[engaged]] = None
						self.free_man.append(engaged)
						self.men_match[self.man[m]] = w
						self.woman_match[self.woman[w]] = m
						break
		print(self.men_match)
		print(self.woman_match)


if __name__ == "__main__":
	
	student_pre = [['d','a','b','c'],
			['c','b','a','d'],
			['c','b','a','d'],
			['d','a','b','c']]
			
	university_pre = [['C','D','B','A'],
			['D','C','A','B'],
			['A','C','B','D'],
			['B','D','A','C']]
	student = {'A':0,'B':1,'C':2,'D':3}
	university = {'a':0,'b':1,'c':2,'d':3}
	
	obj = Gale_Shapely(student,university)
	obj.stable_matching(student_pre,university_pre)

	obj2 = Gale_Shapely(university,student)
	obj2.stable_matching(university_pre,student_pre)