class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def helper(s, no, nc):
            if no == n and nc == n:
                #print(s)
                res.append(s)
                return
            if no < n and no>=nc:
                helper(s+'(' , no+1, nc)
            if  nc < n and no>=nc:
                helper(s+')', no, nc+1 )

            return
        helper('', 0, 0)
        return res
        
