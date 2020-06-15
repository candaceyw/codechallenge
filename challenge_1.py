# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

my_list = [4, 3, 2, 7, 8, 2, 3, 1]

duplicates = []

# for value in my_list:
#     if my_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)


duplicates = list(set([n for n in my_list if my_list.count(n) > 1]))

print(duplicates)

#

# def find_double_elements3(my_list):
#     return list(set([x for x in my_list if my_list.count(x) == 2]))
#
#

# Another solution is still not optimal. It uses sort, so it has O(n log n) runtime.
# It does have O(1) space complexity, though.
# def find_double_elements2(my_list):
#     my_list.sort()
#     pointer = 0
#     while pointer < len(my_list) - 1:
#         if my_list[pointer] != my_list[pointer + 1]:
#             del my_list[pointer]
#         else:
#             pointer += 1
#
#     # print(my_list[:-1])
#     return(my_list[:-1])


#  dictionaries/set solution:
# def find_double_elements5(my_list):
#     lookup = set()
#     pointer = 0
#     while pointer < len(my_list):
#         curr = my_list[pointer]
#         if curr in lookup:
#             pointer += 1
#         else:
#             lookup.add(curr)
#             del my_list[pointer]
# ​
#     return my_list