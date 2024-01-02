# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

def subArr(arr , k):
    n = len(arr)
    lt = []
    for i  in range(n-k+1):
        s = 0
        for j in range(i , i+k):
            s += arr[j]
        lt.append(s/k)
    return lt
    
  #TC : O((n-k)*k) => O(N*K)
  #SC : O(1)  
print(subArr([1, 3, 2, 6, -1, 4, 1, 8, 2] , 5))