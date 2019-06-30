import datetime

nextBirthday = datetime.datetime.strptime('12/20/2014','%m/%d/%Y').date()
currentDate = datetime.date.today()
difference = currentDate - nextBirthday
print(difference.days)