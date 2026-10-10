nums = [2, 7, 11, 15]
target = 9
def two_sum(nums):
    seen = {}
    for index, num in enumerate(nums):
        
        
        if target - num in seen:
            return [seen[target - num], index]
        else:
            seen[num] = index
            