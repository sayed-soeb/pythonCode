'''
Q6. Every other sub-list
Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
E.g.
Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
Return [5, 11, 17, 23]
'''
def get_sublist_with_every_other_element(lst, start_index, end_index):
    sublist = lst[start_index:end_index+1:2]
    return sublist

# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist_with_every_other_element(input_list, start_index, end_index)
print(result)
