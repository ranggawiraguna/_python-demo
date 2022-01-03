import datetime

nowDate = datetime.date.today()
print(type(nowDate), end=' >> ')
print(nowDate)

print(type(nowDate.strftime("%A %B %Y")), end=' >> ')
print(nowDate.strftime("%A %B %Y"))
print()

