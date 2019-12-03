s = input().strip()
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count=1
for i in range(len(s)):
    if s[i] in uppercase : count+=1 
print(count)