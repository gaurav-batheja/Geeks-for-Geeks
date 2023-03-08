# You have a garden with n flowers lined up in a row. 
# The height of ith flower is ai units. You will water them for k days.
# In one day you can water w continuous flowers (you can do this only once in a single day).
# Whenever you water a flower its height increases by 1 unit. You need to maximize the height of the smallest flower all the time.
    def maximizeMinHeight(self, n, k, w, a):
        def check(target):
            days = [0]*n
            operations = 0
            for i in range(n):
                days[i] += days[i-1]
                curr = days[i]
                if a[i]+curr<target:
                    operations += target - a[i] - curr
                    days[i] += target - a[i] - curr
                    if i+w<n:
                        days[i+w] -= target - a[i] - curr
            return operations <= k
                    
        l, r = min(a), max(a)+k
        ans = l
        while l<=r:
            mid = l + (r-l)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
