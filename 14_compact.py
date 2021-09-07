def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # for ele in lst:
    #     if ele is False:
    #         return ele is False
    #         lst.remove(ele)
    # return ele is False

    # new_list = []
    # for ele in lst:
    #     if ele:
    #         new_list.append(ele)
    # return new_list

    return [ele for ele in lst if ele]