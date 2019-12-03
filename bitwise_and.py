t=int(input().strip())
a=[]
for i in range(t):
	a.append(input().split())

for i in range(t):
	max=0
	for j in range(int(a[i][0])):
		for k in range(j+1,int(a[i][0])):
			if (j&k>max) and (j&k<int(a[i][1])):max=j&k
	print(max)
