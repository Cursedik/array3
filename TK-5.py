import math

def task5(listed):
    array = listed
    firstnum = array[0]
    for i in range(len(array)):
        array[i] = math.sqrt(firstnum)
    return array
