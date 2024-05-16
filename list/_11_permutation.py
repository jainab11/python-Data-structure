'''
@Author: Sheikh jainab
@Date: 2024-16-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title :11. Write a Python program to generate all permutations of a list in Python.
'''

def generate_permutations(lst):
    if len(lst) == 0:
        return [[]]  # Base case: return an empty list as a list of permutations of an empty list is itself an empty list
    all_perm = []
    for i in range(len(lst)):
        first_element = lst[i]
        rem_element = lst[:i] + lst[i + 1:]
        for permu in generate_permutations(rem_element):
            all_perm.append([first_element] + permu)
    return all_perm

def main():
    lst = [1, 2, 3]
    result = generate_permutations(lst)
    print(result)

if __name__ == "__main__":
    main()
