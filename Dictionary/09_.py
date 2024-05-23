'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 9. Write a Python program to print a dictionary in table format.

'''

def main():
    my_dict = {'k1':[1,2,3],'k2':[2,3,3],'k3':[3,4,5]}
    for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # Print each row of transposed data as space-separated values.
     print(*row)
if __name__ == "__main__":
    main()
