def ransom_note(magazine, ransom):
    if len(magazine)<len(ransom):
        return False
    mapr={}
    mapm={}
    for i in ransom:
        try : 
            mapr[i] += 1
        except :
            mapr[i] = 1
    for i in magazine:
        try : 
            mapm[i] += 1
        except :
            mapm[i] = 1
    for word in ransom:
        if mapr[word] > mapm[word]:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"