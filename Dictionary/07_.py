'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
def uni_val(my_dict):
    """ pyhton program to print unique val

    Args:
        my_dict (_list_): take a list

    Returns:
        _set_: This function return a set of value with unique numbers
    """
    ans = set()
    for item in my_dict:
        for val in item.values():
         ans.add(val)
    return ans
# This line s = set( val for dic in lis for val in dic.values()) is roughly equivalent to:


 
def main():
    dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    print("original dictionary is : ", dic)
    res = uni_val(dic)
    print("unique values are : ",res)  
         
if __name__ == "__main__":
    main()