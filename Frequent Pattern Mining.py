
# coding: utf-8

# In[ ]:

import itertools
k=int(input())
l=[]
while True:
    try:
        matrix=input()
        l.append(matrix)
    except EOFError:
         break  
l=[[i] for i in l]
f=[]
for i in l:
    a=[words for segments in i for words in segments.split()]
    f.append(a)
#print(f)
length_f=[len(i) for i in f]
max_f=max(length_f)
combinations=[]
for i in range(len(f)):
    lst=f[i]
    for j in range(max_f):
        c = [list(l) for l in itertools.combinations(lst, j)]
        combinations.extend(c)
#print(combinations)
new_list=[sorted(i) for i in combinations]
new_list=[' '.join(x) for x in new_list]
new_list=[i for i in new_list if i != ""]
count_list=list(set(map(lambda x  : (x , list(new_list).count(x)) , new_list)))
update_list=[i for i in count_list if i[1]>=k]
updated_list=sorted(update_list, key=lambda element: (-element[1], element[0]))
for i in updated_list:
    print(i[1],"["+i[0]+"]")
print("")
b=[]
def check(a,b):
    c=0
    for i in b:
        if(i in a):
            c=c+1
        if(c==len(b)):
            return True
for e in updated_list:
    for j in updated_list:
        if e==j:
            continue
        if (check(j[0],e[0])==True):
            if (e[1]<=j[1]):
                break
            if(e[1]>j[1]):
                b.append(e)
b=list(set(b))
#print(b)
d=[]
#print(updated_list)
     
for e in updated_list:
    for j in updated_list:
        if e==j:
            continue
        if(check(j[0],e[0])==True):
            d.append(e)
#print(d)
d=list(set(d))
e=list(set(updated_list) - set(d))
final_list=b+e
final_list=sorted(final_list, key=lambda element: (-element[1], element[0]))
final_list=[i for i in final_list if i[1]>=k]
for i in final_list:
    print(i[1],"["+i[0]+"]")                
    

