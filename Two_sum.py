def two_sum_all_pairs(nums, target):
    lookup = {}
    result = []

    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in lookup:
            result.append([lookup[complement], i])
        
        lookup[num] = i
    
    return result

nums = [2, 7, 11, 2, 6, 3, 15]
target = 9
result = two_sum_all_pairs(nums, target)
print(result)  
