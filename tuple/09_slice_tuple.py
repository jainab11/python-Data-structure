'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title:9. Write a Python program to slice a tuple.
'''
def slice_tuple(my_tuple, start, stop, step):
    return my_tuple[start:stop:step]

def main():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    start = 2  # Starting index (inclusive)
    stop = 7   # Stopping index (exclusive)
    step = 2   # Step size (default is 1 if not specified)
    sliced_tuple = slice_tuple(my_tuple, start, stop, step)
    print("Original Tuple:", my_tuple)
    print("Sliced Tuple:", sliced_tuple)

if __name__ == "__main__":
    main()

    
  

if __name__ == "__main__":
    main()