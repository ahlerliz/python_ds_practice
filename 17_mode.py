def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}

    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    
    biggest_num = 0
    num_to_return = 0

    for key in counter: 
        if counter[key] >  biggest_num:
            num_to_return = key
            biggest_num = counter[key]
    
    return num_to_return
