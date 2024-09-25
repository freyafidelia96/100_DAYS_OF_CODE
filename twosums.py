"""def twoSum(nums, target):
    theSums = []

    for i in range(len(nums)):
        start = i + 1
        for j in range(start, len(nums)):
            if nums[i] + nums[j] == target:
                theSums += [i, j]
    
    return list(set(theSums))
"""

def twoSum(nums, target):
    numbersIndexMap = {}

    for i in range(len(nums)):
        numbersIndexMap[nums[i]] = i

    for j in range(len(nums)):
        key = target - nums[j]
        if key in numbersIndexMap and j != numbersIndexMap[key]:
            return [j, numbersIndexMap[key]]
        
def containsDup(nums):
    numsAsSet = set(nums)
    return len(nums) > len(numsAsSet)

def containsDup2(nums, k):
    dupIndexMap = {}
    for i in range(len(nums)):
        if nums[i] in dupIndexMap and abs(i - dupIndexMap[nums[i]]) <= k:
            return True
        dupIndexMap[nums[i]] = i
    return False      

if __name__ == "__main__":
    results = containsDup2([0,1,3,1], 1)
    print(results)