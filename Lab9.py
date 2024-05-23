def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

def search_2d_array(arr, target):
    for row in arr:
        index = ternary_search(row, target)
        if index != -1:
            return arr.index(row), index
    return None


if __name__ == '__main__':
    rows = int(input("Введіть кількість рядків: "))
    cols = int(input("Введіть кількість стовпчиків: "))

    arr = []
    print("Введіть елементи рядка через пробіл для кожного рядка:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        arr.append(row)

    target = int(input("Введіть ціле число, яке ви хочете знайти: "))

    result = search_2d_array(arr, target)

    if result:
        print(f"Елемент {target} знаходиться у рядку {result[0]} та стовпчику {result[1]}.")
    else:
        print("Елемент не знайдено.")
