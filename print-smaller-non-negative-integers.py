if __name__ == '__main__':
    n = int(input())

    numbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 }

    for num in numbers:
        if num < n:
            print(num * num)