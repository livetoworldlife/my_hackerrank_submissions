if __name__ == '__main__':
    n = int(input())


if 1 <= n <= 20:
    for i in range(n):
        i *= i
        print(i)
else:
    print("Enter between 1 and 20")
