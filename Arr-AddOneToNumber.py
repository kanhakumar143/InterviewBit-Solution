# https://www.interviewbit.com/problems/add-one-to-number/

# Cases
# Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
# A : For the purpose of this question, YES
# Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
# A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def plusOne(self, A):
#         n = len(A)
#         if n < 1:
#             return [1]
#         for i in range(n-1, -1, -1):
#             if A[i] == 9:
#                 A[i] = 0
#             else:
#                 A[i] = A[i] + 1
#                 break
#         if A.count(0) == len(A):
#             A[0] = 1
#             A.append(0)
#         k = 0
#         for i in range(len(A)):
#             if A[i] == 0:
#                 k += 1
#             else:
#                 break
#         return A[k:]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        for i in range(len(A)-1,-1,-1):
            if A[i] != 9:
                A[i] = A[i] + 1
                while A[0] == 0:
                    del A[0]
                break
            else:
                A[i] = 0
        else:
            A.insert(0,1)
        return A

"""
Test
"""
if __name__ == "__main__":
    sol = Solution()
    a = [1, 2, 3]
    
    print(sol.plusOne(a))
"""
Output 
[1, 2, 4]
"""