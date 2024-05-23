'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 1. Write a Python script to sort (ascending and descending) a dictionary by
value.

'''


def main():
    my_dict = {'India':11, 'Turkey':2 ,'Italy':3, 'Paris':4, 'Manchester':5,'USA':6, 'UAE':7}
    # sort by values in reverse order
    print("sort dictionary by keyin reverse order")
    print(sorted(my_dict, reverse =True))
    # sort by key in asending oreder
    print("sort dictionary")
    print(sorted(my_dict))
    print("sort dictionar by values")
    print(dict(sorted(my_dict.items(), key=lambda item: item[1])))
    print("sort dictionary by values in reverse order")
    print(dict(sorted(my_dict.items(), key=lambda item: item[-1],reverse =True)))

  
if __name__ == "__main__":
    main()