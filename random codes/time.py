from datetime import date, datetime

today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)

# to turn it to string
#day of the week %A  day of the month %D fullname of month %B year %Y
print(today.strftime("%A %d %B %Y"))
#replacing attributes
next_year = today.replace(year = today.year + 1)
print(next_year)
difference = abs(next_year - today)
print("only {} till next year".format(difference.days) )
birthdate = date(1980,4,12)
birthdate = date.fromisoformat("1980-04-12")
print(birthdate)
print(birthdate.weekday())

now = datetime.now()
print(now)
print("it's the {}th minute of the {}hr of the {}day of the {}nd".format(
    now.minute, now.hour, now.day, now.month
))

chernobyl = datetime.fromisoformat("1990-04-23 01:23:40:000+04:00")
print("chernobyl occured on" , chernobyl)