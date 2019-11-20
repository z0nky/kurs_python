def my_search(x):
    data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
    data.sort()
    a = 0
    b = len(data) - 1
    while a <= b:
        m = (a + b) // 2
        if x == data[m]:
            return (f'Record {x} found!')
        elif x < data[m]:
            b = data.index(data[m])
        elif x > data[m]:
            a = data.index(data[m + 1])
        elif m == 1:
            return 'record not found'



print(my_search(8))