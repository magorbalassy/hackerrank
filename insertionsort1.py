def printa(arr):
  for i in range(len(arr)) : print(arr[i],end=' ')
  print()

def insertionSort(arr):
  rightmost=arr[len(arr)-1]
  pos=0
  for i in range(len(arr)-2,-1,-1):
    if (arr[i] > rightmost): 
      arr[i+1]=arr[i]
      pos=i
    else :
      break
    printa(arr)
  arr[pos]=rightmost
  printa(arr)

n=int(input().strip())
a=[]
a=input().split()
insertionSort(a)
