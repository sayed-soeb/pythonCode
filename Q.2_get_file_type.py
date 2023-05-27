'''
Q2. Dictionary, what?
Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
'''
def get_file_types(extension_type_string, file_list):
    extension_type_list = extension_type_string.split(';')
    extension_type_dict = {}
    for item in extension_type_list:
        extension, file_type = item.split(',')
        extension_type_dict[extension] = file_type
    
    result_dict = {}
    for file_name in file_list:
        if '.' in file_name:
            extension = file_name.split('.')[-1]
            result_dict[file_name] = extension_type_dict.get(extension, 'unknown')
        else:
            result_dict[file_name] = 'unknown'
    
    return result_dict
extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_types(extension_type_string, file_list)
print(result)
