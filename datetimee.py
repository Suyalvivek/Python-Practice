# DATE
import datetime
date = datetime.date(2004,10,8)
print(date.year)
print(date.month)
print(date.day)

today = datetime.date.today()
print(today)
print(dir(today))
print(today.day)
print(today.month)
print(today.year)
tdelta = datetime.timedelta(days=7)
print(tdelta)
date2 = today+tdelta
print(date2)
print(type(date2))
print(type(today))
print(type(tdelta))

# TIME
time = datetime.time(9,30,24,100)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

# DATETIME
dt = datetime.datetime(2026,6,4,12,57,30,100)
print(dt)
print(dt.date())
print(dt.time())

dt_today = datetime.datetime.today()
print(dt_today)
dt_now = datetime.datetime.now()
print(dt_now)
utc_dt = datetime.datetime.utcnow()
print(utc_dt)


# TIMEZONE AWARE DATE TIME
import pytz
dt = datetime.datetime(2016,7,23,12,30,45,tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
