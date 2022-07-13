#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        zero_cnt = arr.count(0)
        one_cnt = arr.count(1)
        two_cnt = arr.count(2)
        
        arr.clear()
        for i in range(zero_cnt):
            arr.append(0)
        for i in range(one_cnt):
            arr.append(1)
        for i in range(two_cnt):
            arr.append(2)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends