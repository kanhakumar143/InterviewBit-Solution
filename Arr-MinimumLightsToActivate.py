# https://www.interviewbit.com/problems/minimum-lights-to-activate/
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         n = len(A)
#         ans = 0;
#         last = -1;
#         while (last < n - 1):
#             pos = -1
#             end = max(-1,last - B + 1)
#             start = min(n-1,last + B)
#             for i in range( start, end , -1):
#                 if (A[i] == 1 and i - B <= last):
#                     pos = i;
#                     break;
                
            
#             if (pos == -1):
#                 return -1
            
#             ans = ans + 1
#             last = pos + B - 1
        
#         return ans

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i=0
        res=0
        while(i<len(A)):
            j = min(i + B - 1, len(A)-1)
            flag = False
            lb=i-B+1
            if lb<0:
                lb=0
            while(j >=lb):
                if A[j]==1:
                    flag=True
                    res+=1
                    break
                j-=1
            i=j+1+B
            if flag==False:
                return -1
        return res


if __name__ == "__main__":
    sol = Solution()
    a = [ 0, 0, 1, 1, 1, 0, 0, 1]
    b = 3
    print(sol.solve(a,b))