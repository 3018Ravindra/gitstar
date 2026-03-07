# my file for solving DSA Problems with python programming language

# problem is to solve with a print statement
print("Hello DSA")

# Problem is to solve with a variable and a print statement
name = "Ravindra"
print(name)

# Problem is to solve with a variable and a loop
name = "Ravindra"
for char in name:
    print(char)

# Python solution for Two Sum problems
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            # example usage
            nums = [2, 7, 11, 15]
            target = 9
            result = two_sum(nums, target)
            print(result) # output: [0, 1]

            