class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen=set()
        for i in edges:
            if i[0] in seen:
                return i[0]
            elif i[1] in seen:
                return i[1]
            else:
                seen.add(i[0])
                seen.add(i[1])
