def diff(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    differnce = set1-set2
    return list(differnce)
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
result = diff(lst1, lst2)
print("Difference between the two lists:", result)
    