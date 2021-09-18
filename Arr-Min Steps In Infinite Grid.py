# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
# 
# class Solution:
# 	# @param A : list of integers
# 	# @param B : list of integers
# 	# @return an integer
# 	def coverPoints(self, A, B):
#         prevx = A[0]
#         prevy = B[0]
#         n = len(A)
#         ans = 0
#         for i in range(1,n):
#             curx = A[i]
#             cury = B[i]
#             diffx = abs(curx-prevx)
#             diffy = abs(cury-prevy)
#             ans += max(diffx, diffy)
#             prevx = curx
#             prevy = cury
#         return ans

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        for i in range(len(A)-1):
            pt1 = (A[i],B[i])
            pt2 = (A[i+1],B[i+1])
            distance = self.distanceBtwnPoints(pt1,pt2)
            steps += distance
            
            # print(pt1, pt2, distance)
            
        return steps
        
    def distanceBtwnPoints(self, pt1, pt2):
        return max(abs(pt1[0]-pt2[0]), abs(pt1[1]-pt2[1]))

if __name__ == "__main__":
    sol = Solution()
    a = [0, 1, 1]
    b = [0, 1, 2]
    print(sol.coverPoints(a,b))