# Как сделал
def selection_sort(numbers: list) -> list:
    cursor = 0
    for i in range(len(numbers)):
        _min = numbers[cursor]
        _count = 0
        for k, v in enumerate(numbers[cursor:], cursor):
            if _min >= v:
                _min = v
                _count = k

        number = numbers.pop(_count)
        numbers.insert(cursor, number)
        cursor += 1

    return numbers

# Решение лучше (забыл про перестановку значений в одну строку)
#def sel_sort(row):
#    n = len(row)
#    for i in range(n-1):
#        m = i
#        for j in range(i+1, n):
#            if row[j] < row[m]:
#                m = j
#        row[i], row[m] = row[m], row[i]


assert selection_sort([]) == []
assert selection_sort([3,2,1]) == [1,2,3]
assert selection_sort([3,4,3,2,1]) == [1,2,3,3,4]

