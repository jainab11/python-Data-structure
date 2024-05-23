'''

@Author: Jainab sheikh

@Date: 2024-05-23

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-23

@Title :10. Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
'''
def main():
    my_dict = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
    False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    print(sum(ele['id'] for ele in my_dict))
    print(sum(ele['success'] for ele in my_dict))
    

        
 
if __name__ == "__main__":
    main()