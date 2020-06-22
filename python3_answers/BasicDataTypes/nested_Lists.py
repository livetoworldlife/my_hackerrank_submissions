if __name__ == '__main__':
    a = int(input())
    liste = []
    scores = []
    son = []
    for _ in range(a):
        name = input()
        score = float(input())
        liste.insert(_,[name,score])
        scores.append(score)

second = sorted(list(set(scores)))[1]
liste.sort()

for nm,sc in liste:
    if sc == second:
        print(nm)
        
