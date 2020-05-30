# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

from typing import List, Union

def sum_of_intervals(list_of_intervals:list)->int:
    list_of_intervals.sort()
    for intervals in range(len(list_of_intervals) - 1):
        if list_of_intervals[intervals][1] >=  list_of_intervals[intervals + 1][0]:
            if list_of_intervals[intervals][1] <= list_of_intervals[intervals + 1][1]:
                list_of_intervals[intervals + 1] = \
                    [list_of_intervals[intervals][0],list_of_intervals[intervals + 1][1]]
                list_of_intervals[intervals] = None
            else:
                list_of_intervals[intervals + 1] = list_of_intervals[intervals]
                list_of_intervals[intervals] = None
    
    remove_sign = list(filter(None, list_of_intervals))

    return sum(list(map(lambda x: x[1] - x[0],remove_sign)))
