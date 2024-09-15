#This is a code to find sum of two numbers from a list of numners whose sum is equal to a target number
#Here we write a function with two parameters nums and target.
def two_sum_all_pairs(nums, target):
    #we define and initialize a dictionary lookup to store desired element from the list num as well as its index
    #we also define and initialize a list called result where we store the result
    lookup = {}
    result = []
    #for each of the index as well as element in the list num we run this loop
    for i, num in enumerate(nums):
        # we calculate the difference between the taget and each element of nums abd store it in compliment 
        complement = target - num
        
        if complement in lookup:
            result.append([lookup[complement], i])
        
        lookup[num] = i
    
    return result

nums = [2, 7, 11, 2, 6, 3, 15]
target = 9
result = two_sum_all_pairs(nums, target)
print(result)  
