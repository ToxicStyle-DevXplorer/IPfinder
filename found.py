def binary_search(array,x):
    Lenth = 0
    Rotation = len(array) - 1
    while Lenth <= Rotation:
        Middle = (Lenth + Rotation) // 2
        if array[Middle] < x:
            Lenth = Middle + 1
        elif array[Middle] > x:
            Rotation = Middle - 1
        else:
            return Middle
    return -1

print(binary_search([1,2,3,4,5,6], 5))