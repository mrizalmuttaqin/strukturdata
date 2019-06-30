import datetime
birthday = input("What is your birthday? ")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print("Your birth month is " + birthdate.strftime('%B'))