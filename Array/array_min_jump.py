#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
	    #code here
        i = 0
        jump = 0
        while(i<n):
            max_index_to_jump = 0
            max_value_to_jump = 0
            
            if i+arr[i]+1 < n:
                max_iterate = i+arr[i]+1
                for j in range(i+1,max_iterate):
                    if j+arr[j] >= max_value_to_jump:
                        max_index_to_jump = j
                        max_value_to_jump = j+arr[j]
            else:
                if (i == 0) and (arr[i] == 0):
                    max_index_to_jump  = 0
                else:
                    max_index_to_jump = n

            

            if max_index_to_jump == 0:
                return -1
            else:
                jump+=1
                i=max_index_to_jump
        return jump
	                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    s = Solution()
    # print(s.minJumps([2,3,1,1,2,4,2,0,0,1,1],10))
    # print(s.minJumps([2,0,0,0,0],5))
    # print(s.minJumps([1,3,5,8,9,2,6,7,6,8,9],11))
    print(s.minJumps([0],1))
# } Driver Code Ends