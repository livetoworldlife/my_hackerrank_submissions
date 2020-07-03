def minion_game(string):
    seli_k = 0
    sesiz_s = 0
    
    string = string.upper()
    #print(string)
    vowels = 'AEIOU'
    
    for i in range(len(string)):
        if string[i] in vowels:
            seli_k += (len(string)-i)
        else:
            sesiz_s += (len(string)-i)

    if seli_k > sesiz_s:
        print("Kevin", seli_k)
    elif seli_k < sesiz_s:
        print("Stuart", sesiz_s)
    else:
        print("Draw")
