#Хорошее решение
def insertion_sort(numbers: list) -> list:
    for i in range(1, len(numbers)):
        k = i
        while k > 0:
            if numbers[k-1] > numbers[k]:
                numbers[k-1], numbers[k] = numbers[k], numbers[k-1]
            k -= 1

    return numbers

print(insertion_sort([4, 22, 41, 40, 27, 31, 36, 1, 42, 39, 14, 9, 3, 6, 34, 9, 21, 4, 29, 49]))
assert insertion_sort([]) == []
assert insertion_sort([3,2,1]) == [1,2,3]
assert insertion_sort([3,4,3,2,1]) == [1,2,3,3,4]
assert insertion_sort([12, 11, 13, 5, 6]) == [5,6,11,12,13]
