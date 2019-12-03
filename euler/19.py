'''
How many Sundays fell on the first of the month between two dates(both inclusive)?
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date
from datetime import datetime
from datetime import timedelta
from calendar import monthrange

days_in_month = lambda dt: monthrange(dt.year, dt.month)[1]

t = int(raw_input().strip())
start_date=[]
end_date=[]
results=[]
for a0 in xrange(t):
    a, b, c = tuple(int(x.strip()) for x in raw_input().split())
    start_date.append(date(a,b,c))
    a, b, c = tuple(int(x.strip()) for x in raw_input().split())
    end_date.append(date(a,b,c))
    count = 0
    s_date = start_date[a0]
    e_date = end_date[a0]
    if s_date.day !=1 :
        s_date = s_date.replace(day=1) + timedelta(days_in_month(s_date))
    while True :
        if (s_date.weekday()==6) and (s_date.day==1) : count+=1
        s_date = s_date.replace(day=1) + timedelta(days_in_month(s_date))
        if s_date >= e_date : break
    results.append(count)
for x in results: print x