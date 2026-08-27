from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        student_counts = Counter(students)

        for s in sandwiches:
            if student_counts[s] > 0:
                student_counts[s] -= 1
                res -= 1
            else:
                break
        
        return res
        


