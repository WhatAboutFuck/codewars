#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

from typing import List

def solution(string: str, markers: List[str])->str:
    if string == "":
        return string
    string = string.splitlines()
    merge = []
    for word in string:
        s = ''
        for letter in word:
            if letter not in markers:
                s += letter
            else:
                break
        merge.append(s.rstrip())
    return '\n'.join(merge)
