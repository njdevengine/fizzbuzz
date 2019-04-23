import datetime
a = datetime.datetime.now()
if a.isoweekday() == 6:
    a += datetime.timedelta(days=2)
    a = a.replace(hour=9,minute=0,second=0,microsecond=0)
    now = datetime.datetime.now()
    c = a - now
    wait_time = c.seconds
    time.sleep(wait_time)
elif a.isoweekday() == 7:
    a += datetime.timedelta(days=1)
    a = a.replace(hour=9,minute=0,second=0,microsecond=0)
    now = datetime.datetime.now()
    c = a - now
    wait_time = c.seconds
    time.sleep(wait_time)
