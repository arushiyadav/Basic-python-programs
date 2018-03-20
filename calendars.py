import calendar
print(calendar.calendar(2018,1,2,3))
print("the number of first week day (monday)",calendar.firstweekday())
print("month starting day number and no. of days it have",calendar.monthrange(2018,2))
#without writing print displaying calendar
calendar.prcal(2017)
calendar.prmonth(2018,8,1,1)
#defining the starting day no. as 1
calendar.setfirstweekday(1)
print("now the starting wee day no. is",calendar.firstweekday())
print(" specified date is 23rd august 2018 and the week day no. is",calendar.weekday(2018,8,23))
