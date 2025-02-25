def closest_to_zero(nums):
    return min(nums, key = lambda x:(abs)(x))
list=[-1, 4, 2, 10, 70]
print(closest_to_zero(list))