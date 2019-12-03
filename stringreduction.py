# Head ends here
def stringReduction(a):
    switcher = {
        "ab": "c",
        "ac": "b",
        "ba": "c",
        "bc": "a",
        "ca": "b",
        "cb": "a"
    }
    lst=list(a)
    i=0
    c=''
    while i<len(lst)-1:
        if lst[i]!=lst[i+1] : 
            c=switcher.get(str(lst[i]+lst[i+1]))
            lst.insert(i+2,c)
            del lst[i:i+2]
            i=0
        else:
            i+=1
    return len(lst)

# Tail starts here
if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        a=input()
        print(stringReduction(a))
