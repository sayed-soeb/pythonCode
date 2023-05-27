'''
Q3. Column Sorting, yay!
Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]
AND
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "color")
Should Output
[
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"}
]
'''

def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

# Example usage
list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
key = "fruit"

sorted_list = sort_list_of_dicts(list_of_dicts, key)
print(sorted_list)

