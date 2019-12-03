import math

# calculate next nr in the chain
def calc_next(nr):
  str_from_nr=str(nr)
  next_nr=0
  for i in range(len(str_from_nr)):
    figure=int(str_from_nr[i])
    next_nr=next_nr+(figure*figure)
  return next_nr

def main():
  target=int(input().strip())
  target=pow(10,target)
  count=0
  next_nr=0
  for i in range(1,target+1):
    next_nr=calc_next(i)
    while (next_nr != 1) and (next_nr != 89) :
      next_nr=calc_next(next_nr)
    if next_nr == 89 : count+=1
  print(count)


if __name__ == "__main__":
  main()