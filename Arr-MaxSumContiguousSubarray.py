# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxSubArray(self,a):
        
#         mx = a[0]
#         curr_max = a[0]

#         for i in range(1, len(a)):
#             curr_max = max(a[i], curr_max + a[i])
#             mx = max(mx, curr_max)

#         return mx
#     if __name__ == "__main__":
#         a = []
#         l = len(a)
#         for i in range(0, n):
#             ele = int(input())
#             a.append(ele)  
        
#         x = maxSubArray(a)
#         print(x)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n=len(A)
        smax=-1000
        lmax=0
        for a in A:
            lmax+=a
            if lmax>smax:
                smax=lmax
            if lmax<0:
                lmax=0
        return smax

if __name__ == "__main__":
    sol = Solution()
    A = [1, 2, 3, 4, -10]
    print(sol.maxSubArray(A))
        
