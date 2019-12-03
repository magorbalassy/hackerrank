contacts={}
for i in range(97,123):
    contacts[chr(i)]=[]
    for j in range(97,123):
        contacts[chr(i),chr(j)]=[]
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add' :
        contacts[contact[0]].append(contact)
        if len(contact)>1:
        	contacts[contact[0],contact[1]].append(contact)
    elif op == 'find' :
        n = len([c for c in contacts[contact[0],contact[1]] if c.find(contact)==0])\
          if len(contact)>1\
          else\
          len([c for c in contacts[contact[0]] if c.find(contact)==0])
        print n