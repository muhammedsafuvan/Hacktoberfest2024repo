def solve(arr,n,k):
    ans,res = arr[0],arr[0]
    s = 0
    for i in range(n-k):
        res = sum(arr[i:i+k])
        ans = max(ans,res)
    return ans
            
arr = [-1,-2,3,1,-3,2]
n = len(arr)
k = 2
print(solve(arr,n,k))
        
