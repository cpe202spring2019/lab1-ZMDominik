
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if len(int_list) == 0:
        return None
    elif int_list is None:
        raise ValueError
    max_int = -99999
    for num in int_list:
        if num > max_int:
            max_int = num
    return max_int


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        return ValueError

    if len(int_list) == 1:
        return int_list
    elif len(int_list) == 2:
        return [int_list[-1], int_list[0]]
    temp1 = [int_list[-1]]
    temp2 = [int_list[0]]
    return temp1+reverse_rec(int_list[1:-1])+temp2

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        return ValueError

    min = low
    max = high
    found = False
    while not found and min < max:
        mid = (min+max)//2
        if int_list[mid] == target:
            return mid
        else:
            if int_list[mid] > target:
                max = mid-1
            elif int_list[mid] < target:
                min = mid+1
    return None