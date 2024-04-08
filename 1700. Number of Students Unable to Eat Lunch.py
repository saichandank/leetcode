class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        i=0
        j=0
        while students and sandwiches:
            
            if students[0]==sandwiches[0]:
                sandwiches=sandwiches[1:]
                count=0
            else:
                count+=1
                students.append(students[0])

            students=students[1:]

            if count==len(students):
                return count

        return 0

            
        
