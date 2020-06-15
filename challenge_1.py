# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

a = [4, 3, 2, 7, 8, 2, 3, 1]

duplicates = []

# for value in a:
#     if a.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)


duplicates = list(set([x for x in a if a.count(x) > 1]))
print(duplicates)