def array_left_rotation(a, n, k):
    res = []
    for r in a[k:] :
    	res.append(r)
    for r in a[:k]:
    	res.append(r)
    return res

    

#n, k = map(int, raw_input().strip().split(' '))
#a = map(int, raw_input().strip().split(' '))
n=5
k=4
a=[1,2,3,4,5]
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
