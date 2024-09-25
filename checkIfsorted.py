# def checkIfSorted(listInput):
#     lengthOflist = len(listInput)
#     pivot = 1
#     key = listInput[pivot]

#     for element in listInput:
#         if pivot != (lengthOflist - 1):
#             pivot += 1
#         if key < element:
#             return False
#         else:
#             key = listInput[pivot]
#             continue

#     return True

def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True 

if __name__ == "__main__":
    results = is_sorted([22])

    print(results)