def task4(listed):
    array = listed
    sum_arr = sum(array)
    arr_avg = sum_arr/len(array)
    for i in range(len(array)):
        array[i] = array[i]*arr_avg
    return array
