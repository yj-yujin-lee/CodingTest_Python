def rec(n,k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k % 2:
        return 1+min(rec(n, k-1), rec(n, k+1))
    else:
        return min(k-n, 1 + rec(n, k//2))
    
n, k = map(int, input().split())
print(rec(n, k))