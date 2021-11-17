# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum( nums, target):
# define hash map to sort out complements 
    hash_map = {}
# loop through to find if any two element equals the target
    for i in range(len(nums)):
        complement = target - nums[i]
# add complement to hash_map if it does not exist already
        if complement not in hash_map:
            hash_map[nums[i]] = nums[i]
        else:
# if complement exists, a match is found and return indices
            indexSums = [i, nums.index(complement)]
            return indexSums

print(twoSum([3, 3], 6))

# def hash_func(input_str, tbl_size):
#     string = input_str.encode()
#     sum = 0
#     for s in string:
#         sum += s
#     return sum 

# print(hash_func("saeed", 10))