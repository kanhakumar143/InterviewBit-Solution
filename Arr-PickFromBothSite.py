
# Example Input
# Input 1:

#  A = [5, -2, 3 , 1, 2]
#  B = 3
# Input 2:

#  A = [1, 2]
#  B = 1


# Example Output
# Output 1:

#  8
# Output 2:

#  2
#  https://www.interviewbit.com/problems/pick-from-both-sides/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def solve(self, A, B):

    #     Sum = Max = sum(A[:B])
    #     N = len(A)
    #     for i in range(1, B+1):
    #         Sum = Sum - A[B - i] + A[N - i]
    #         if Sum > Max:
    #             Max = Sum
    #     return Max

    def solve(self, A, B):
        arr=A[:B]               #Array of present sum
        val=sum(A[:B])  
        imax=val
        for i in range(0,B):
            rem=arr.pop()       #Remove the last element from arr
            add=A.pop()         #Last element of A
            val=val-rem+add     #Remove the last element of arr and replace it with last element of A
            imax=max(imax,val)
        return imax

    # def solve(self, A, B):
    #     current_sum = sum(A[:B])
    #     max_sum = current_sum
    #     if B < len(A):
    #         for i in reversed(range(B)):
    #             current_sum += -A[i] + A[i - B]
    #             if current_sum > max_sum:
    #                 max_sum = current_sum
    #     return max_sum
        

        

if __name__ == "__main__":
    sol = Solution()
    a = [5, -2, 3, 1, 2]
    # a = 2
    b = 3
    print(sol.solve(a,b))


    