n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
swaps = 0

for i in range(n): 
    for j in range(n-1) :
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1] :
            t = a[j]
            a[j]=a[j + 1]
            a[j+1]=t
            swaps += 1


print "Array is sorted in %d swaps." % swaps
print "First Element: %d" % a[0] 
print "Last Element: %d" % a[len(a)-1]