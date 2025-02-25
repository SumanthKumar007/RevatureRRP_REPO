lis = [23,45,32,10,35]
def second_largest(nums):
    return sorted(set(nums))[-2]
print(second_largest(lis))
