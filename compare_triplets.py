a=list(input().split())
b=list(input().split())

score_a=0
score_b=0

for i in range(3):
	if int(a[i]) > int(b[i]):
		score_a+=1
	if int(a[i]) < int(b[i]):
 		score_b+=1

print(score_a,score_b)