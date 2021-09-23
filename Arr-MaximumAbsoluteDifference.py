# https://www.interviewbit.com/problems/maximum-absolute-difference/

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        ap = []
        am = []
        for i in range(len(A)):
            ap.append(A[i]+i)
            am.append(A[i]-i)
        m1, m2 = (min(ap), max(ap))
        m3, m4 = (min(am), max(am))

        return max(abs(m1-m2), abs(m3-m4))

"""
Test
"""
if __name__ == "__main__":
    sol = Solution()
    A=[1, 3, -1]
    
    print(sol.plusOne(A))
"""
Output 
5
"""