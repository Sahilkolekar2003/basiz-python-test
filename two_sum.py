def two_sum(nums, target):
    lookup={}

    for i, num in enumerate(nums):
        complement = target - num       
        if complement in lookup:
            return [lookup[complement], i]      
        lookup[num]=i
    return[]

print(two_sum([2, 7, 11, 15], 9))