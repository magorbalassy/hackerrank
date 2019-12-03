import re

def is_matched(expression):
    par = True
    temp = expression
    while par :
        t = len(temp)
        temp = re.sub('\(\)','',expression)
        if len(temp) < len(expression) :
            expression = temp
        temp = re.sub('\[\]','',expression)
        if len(temp) < len(expression) :
            expression = temp
        temp = re.sub('\{\}','',expression)
        if len(temp) < len(expression) :
            expression = temp
        if len(temp) == t :
            par = False
        if len(expression) == 0 :
            return True
    if len(temp) != 0 :
        return False
    else :
        return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
