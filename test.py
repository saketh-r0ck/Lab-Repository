class Gale_Shapely:
    def __init__(self, proposing, proposed):
        self.student_match = [None] * len(proposing)
        self.university_match = [None] * len(proposed)
        self.free_student = list(proposing.keys())
        self.student = proposing
        self.university = proposed

    def stable_matching(self, student_preference, university_preference):
        while len(self.free_student) > 0:
            s = self.free_student.pop(0)

            s_list = student_preference[self.student[s]]
            for u in s_list:
                university_idx = self.university[u]
                engaged = self.university_match[university_idx]
                if engaged is None:
                    self.student_match[self.student[s]] = u
                    self.university_match[self.university[u]] = s
                    break
                else:
                    u_list = university_preference[university_idx]
                    if u_list.index(s) < u_list.index(engaged):
                        self.student_match[self.student[engaged]] = None
                        self.free_student.append(engaged)
                        self.student_match[self.student[s]] = u
                        self.university_match[self.university[u]] = s
                        break

        for i in self.student:
            print(i + " -> " + self.student_match[self.student[i]])

if __name__ == "__main__":

    student_pre = [['d', 'a', 'b', 'c'],
                   ['c', 'b', 'a', 'd'],
                   ['c', 'b', 'a', 'd'],
                   ['d', 'a', 'b', 'c']]

    university_pre = [['C', 'D', 'B', 'A'],
                      ['D', 'C', 'A', 'B'],
                      ['A', 'C', 'B', 'D'],
                      ['B', 'D', 'A', 'C']]
    student = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    university = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    print("Student oriented:")
    obj = Gale_Shapely(student, university)
    obj.stable_matching(student_pre, university_pre)
    print("University oriented")
    obj2 = Gale_Shapely(university, student)
    obj2.stable_matching(university_pre, student_pre)
