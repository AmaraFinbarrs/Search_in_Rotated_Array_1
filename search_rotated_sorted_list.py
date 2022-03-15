# Write a program to find the position of a target in a sorted list rotated an unknown number of times

# function to conduct binary search
def binary_search(lo, hi, nums, condition):
    while lo <= hi:

        mid = (lo + hi) // 2
        mid_number = nums[mid]
        print("lo:", lo, ", hi:", hi, ", mid_number", mid_number)
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
        else:
            return -1

    return -1


# This function would be used to find the condition of the target position relative to the middle of the element and the smallest element. It would accept the target, mid and the last position as inputs and return the condition
# 'left', 'right', or 'found' as outputs
def search_sorted_array(nums, target):
    def condition(mid):

        # First we find the middle element
        # we check if target is the middle element, then if it is, we return 'found'. if not, next step.
        if nums[mid] == target:
            return 'found'

        # special case: the list contains one element but not the target element
        elif nums[mid] != target and len(nums) == 1:
            return 'does not exist'

        # We check for some obvious cases
        # Case 1: if target is greater than the middle number and greater than the last number on the list, then it is
        # positioned on the left of the middle number. we return 'left'.
        elif target > nums[mid] and target > nums[len(nums) - 1]:
            # Case 1a: if the target is greater than the middle number and greater than the last number,
            # the target is on the left only if the smallest number is on the left. We know the smallest number
            # is on the left because the middle number is greater than its predecessor and less than or equal to
            # the last number. we return 'left'.
            if nums[mid - 1] < nums[mid] <= nums[len(nums) - 1]:
                return 'left'

            # Case 4b: if the target is less than the middle number and less than or equal the last number,
            # the target is on the right only if the smallest number is on the right. We know the smallest number is on
            # the right because the middle number is greater than its predecessor and greater than the last number.
            # we return 'right'.
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[len(nums) - 1]:
                return 'right'

            # Case 4c: if the middle number is the smallest number, then the target is the left.
            elif nums[mid] < nums[mid - 1]:
                return 'left'

        # Case 2: if target is less than the middle number and greater than the last number, it is also on the left side
        # of the middle number. we return 'left'.
        elif nums[mid] > target > nums[len(nums) - 1]:
            return 'left'

        # Case 3: if target is greater than the middle number and less or equal to the last number, then target is
        # positioned on the right. we return 'right'.
        elif nums[mid] < target <= nums[len(nums) - 1]:
            return 'right'

        # However, it is not straightforward to say if the target is on the left or right, when it is less than
        # the middle number and less than or equal to the last number. This is due to the sorted nature of the list.
        # We need a better determinant for this condition. This leads to Case 4a and Case 4b.
        elif target < nums[mid] and target <= nums[len(nums) - 1]:

            # Case 4a: if the target is less than the middle number and less than or equal the last number,
            # the target is on the left only if the smallest number is on the left. We know the smallest number
            # is on the left because the middle number is greater than its predecessor and less than or equal to
            # the last number. we return 'left'.
            if nums[mid - 1] < nums[mid] <= nums[len(nums) - 1]:
                return 'left'

            # Case 4b: if the target is less than the middle number and less than or equal the last number,
            # the target is on the right only if the smallest number is on the right. We know the smallest number is on
            # the right because the middle number is greater than its predecessor and greater than the last number.
            # we return 'right'.
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[len(nums) - 1]:
                return 'right'

    return binary_search(0, len(nums) - 1, nums, condition)




# module to used to check different test cases easily.
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

# different test cases
# The smallest element is in the middle of the list; test0, test1 and test2.
# The target is in the middle
test0 = {
    'input': {
        'nums': [6, 7, 8, 1, 2, 3, 4, 5],
        'target': 1
    },
    'output': 3
}

# The is in the first half of the list (the beginning)
test1 = {
    'input': {
        'nums': [6, 7, 8, 1, 2, 3, 4, 5],
        'target': 6
    },
    'output': 0
}

# The target is in the second half of the list (the end)
test2 = {
    'input': {
        'nums': [6, 7, 8, 1, 2, 3, 4, 5],
        'target': 5
    },
    'output': 7
}

# The smallest element of the list is in the first half of the list; test3, test4, test5.

# the target is at the middle of the list
test3 = {
    'input': {
        'nums': [7, 8, 1, 2, 3, 4, 5, 6],
        'target': 2
    },
    'output': 3
}

# The target is on the left side of the smallest element
test4 = {
    'input': {
        'nums': [7, 8, 1, 2, 3, 4, 5, 6],
        'target': 8
    },
    'output': 1
}

# The target is on the right side of the element
test5 = {
    'input': {
        'nums': [7, 8, 1, 2, 3, 4, 5, 6],
        'target': 4
    },
    'output': 5
}

# The list is the first element of the list meaning that the list was rotated zero/n times. n is the size of the list.
# test6, test7, test8

# the target is at the middle of the list
test6 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target': 5
    },
    'output': 4
}

# the target is at the beginning or first half of the list
test7 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target': 2
    },
    'output': 1
}

# the target is at the end or the second half of the list
test8 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target': 8
    },
    'output': 7
}

# the smallest number is at the end of the list-meaning that the list rotated n-1 times; test9, test10, test11, test12.

# the target is at the middle of the list
test9 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1],
        'target': 5
    },
    'output': 3
}

# the target is at the first half of the list
test10 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1],
        'target': 3
    },
    'output': 1
}

# the target is at the second half of the list
test11 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1],
        'target': 8
    },
    'output': 6
}

# the target is at the end of the list
test12 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1],
        'target': 1
    },
    'output': 7
}

# the smallest number in the list is positioned in the second half, the list rotated n-2 times. test13, test14

# the target is at the n-2 position
test13 = {
    'input': {
        'nums': [3, 4, 5, 6, 7, 8, 1, 2],
        'target': 1
    },
    'output': 6
}

# the target is on the first half
test14 = {
    'input': {
        'nums': [3, 4, 5, 6, 7, 8, 1, 2],
        'target': 4
    },
    'output': 1
}

# smallest number is the only number
test15 = {
    'input': {
        'nums': [5],
        'target': 5
    },
    'output': 0
}

# the target is not on the list
test16 = {
    'input': {
        'nums': [6, 7, 8, 1, 2, 3, 4, 5],
        'target': 3.5
    },
    'output': -1
}

# list rotated just once. test17, test18, test19

# target is the first element
test17 = {
    'input': {
        'nums': [8, 1, 2, 3, 4, 5, 6, 7],
        'target': 8
    },
    'output': 0
}

# target is at the first half of the element
test18 = {
    'input': {
        'nums': [8, 1, 2, 3, 4, 5, 6, 7],
        'target': 2
    },
    'output': 2
}

# target is at the second half of the list
test19 = {
    'input': {
        'nums': [8, 1, 2, 3, 4, 5, 6, 7],
        'target': 6
    },
    'output': 6
}

# target is at the second half of the list
test20 = {
    'input': {
        'nums': [4, 5, 6, 7, 0, 1, 2],
        'target': 0
    },
    'output': 4
}

# the list contains one element but not the target
test21 = {
    'input': {
        'nums': [2],
        'target': 0
    },
    'output': -1
}

# the list contains no element
test22 = {
    'input': {
        'nums': [],
        'target': 0
    },
    'output': -1
}


tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15, test16, test17, test18, test19, test20, test21, test22,]

# to check one test case
#evaluate_test_case(search_sorted_array, test21)

# to check all test cases
evaluate_test_cases(search_sorted_array, tests)
