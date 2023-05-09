# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/9/23
# Description: This code takes a list of numbers as input and returns the maximum value in the list. The function works
# by breaking the list into two parts, finding the maximum value in each part, and returning the maximum of those
# two values.

def list_max(lst):
    """
    Recursive function that returns the maximum value in a list of numbers.
    
    lst: A list of numbers. Cannot be empty.
    """
    if len(lst) == 1:
        return lst[0]
    else:
        left_max = list_max(lst[:len(lst)//2])
        right_max = list_max(lst[len(lst)//2:])
        return left_max if left_max > right_max else right_max
