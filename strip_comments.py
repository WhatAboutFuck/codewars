def solution(string, markers):
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
