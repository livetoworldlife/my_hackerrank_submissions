n = 1
liste = []

sayi = int(input())
while n < sayi + 1:
    other_input = str(input())
    n += 1
    
    if len(other_input.split()) == 3:
        komut, indx, elm = other_input.split()
    elif len(other_input.split()) == 2:
        komut, elm = other_input.split()
    elif len(other_input.split()) == 1:
        komut = other_input
    else:
        print("Enter correct inputs")

    
    if komut == "insert":
        liste.insert(int(indx),int(elm))
    elif komut == "print":
        print(liste)
    elif komut == "remove":
        liste.remove(int(elm))
    elif komut == "append":
        liste.append(int(elm))
    elif komut == "sort":
        liste.sort()
    elif komut == "pop":
        liste.pop()
    elif komut == "reverse":
        liste.reverse()
    else:
        print(komut, liste)

    
   

