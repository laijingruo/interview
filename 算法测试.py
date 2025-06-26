def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []


nums = [5, 6, 8, 10, 16, 20]
target = 30
print(twoSum(nums, target))