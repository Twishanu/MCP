nums = [1,7,68,2,2,13,7,1]
nums_set = {num for num in nums}
print(nums_set)

num_pairs = {
    "odd" : [1,3,5,7,9],
    "even": [2,4,6,8,10],
    "prime": [2,3,5,7,11]
}

unique_num_set = {num for nums in num_pairs.values() for num in nums}
print(unique_num_set)