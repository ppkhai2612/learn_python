import datetime as dt

date_obj = dt.datetime.strptime(
    '31/01/22 23:59:59.999999',
    '%d/%m/%y %H:%M:%S.%f')

date_str = date_obj.strftime('%a %d %b %Y, %I:%M%p')

print(date_obj)
print(date_str)