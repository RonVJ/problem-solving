

def max_container(self, arr):
    l = 0
    n = len(arr)
    r = n-1
    max_area = 0

    while l < r:
        area = min(arr[r],arr[l]) * (r-l)
        max_area = max(max_area, area)
        if arr[l] < arr[r]:
            l = l+1
        else:
            r = r-1
    return max_area


