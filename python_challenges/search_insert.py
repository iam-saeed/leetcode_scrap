#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
    if target not in nums:
        nums.append(target)
        nums.sort()
        return nums.index(target)
    else:
        return nums.index(target)

print(searchInsert([1,3,5,6], 5))