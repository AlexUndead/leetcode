import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    count = int(input())
    coordinates = [int(c) for c in input().split()]
    coordinates.sort()
    if len(coordinates) < 4:
        result = coordinates[-1] - coordinates[0]
    else:
        result = coordinates[1] - coordinates[0]

        for i, values in enumerate(coordinates[3:], 3):
            if i == len(coordinates) - 1:
                result += values - coordinates[i - 1]
            else:
                result += min(coordinates[i - 1] - coordinates[i - 2], values - coordinates[i - 1])
                
    print(result)


if __name__ == '__main__':
    main()
