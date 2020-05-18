if __name__ == '__main__':
    n = int(input())

liste = []
for i in range(1, n + 1):
    liste.append(i)

print(*liste, sep='')
