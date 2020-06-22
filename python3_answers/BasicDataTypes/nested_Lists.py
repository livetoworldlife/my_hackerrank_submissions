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
        

# second solution        
if __name__ == '__main__':
    a = int(input())
    marksheet = []
    
    for _ in range(a):
        name = input()
        score = float(input())
        marksheet.append([name, score])
        

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
