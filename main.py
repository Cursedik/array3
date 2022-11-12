import importlib
from TK_1 import task1
from TK_2 import task2
from TK_3 import task3
from TK_4 import task4
sub = importlib.import_module('TK-5')
def main(arr):
    tk3 = arr
    tk4 = arr
    tk5 = arr
    print("Calling first function from TK_1")
    print(task1(10))

    print("Calling first function from TK_2")
    print(task2(list))

    print("Calling first function from TK_3")
    print(task3(tk3))

    print("Calling first function from TK-4")
    print(task4(tk4))

    print("Calling first function from TK-5")
    print(sub.task5(tk5))

    return 0
list = [64, 1, 4, 65, 109, 5]
main(list)
