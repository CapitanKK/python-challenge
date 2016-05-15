import datetime

for i in range(99, 1, -2):
    d = datetime.date(1000 + i * 10 + 6, 1, 1)
    if d.weekday() == 3:
        print(d.year)