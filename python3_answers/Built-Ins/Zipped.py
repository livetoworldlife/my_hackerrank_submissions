o_n = list(map(int, input().split()))

ogrenci = o_n[0]
notes = o_n[1]
common_list = list()

for i in range(notes):
    not_list = list(map(float, input().split()))
    common_list.append(not_list)
    
for i in zip(*common_list): 
    print( sum(i)/len(i) ) 
