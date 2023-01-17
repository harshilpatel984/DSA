#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        arr_set = []
        for i in range(N):
            for j in range(N):
                arr_set.append(Mat[i][j])
            
        arr_set = list(sorted(arr_set))
        
        new_arr = []
        upper = 0
        lower=N
        for i in range(N):
            new_arr.append(arr_set[upper:lower])
            upper+=N
            lower+=N
        
        return new_arr
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends