s = input().upper()
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count=0
for i in range(len(uppercase)):
    if uppercase[i] in s : count+=1 
if count==26 :
	print("pangram")
else :
	print("not pangram")